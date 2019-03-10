
"""This script nuke all glacier resources"""

import boto3


def nuke_all_glacier(logger):
    """
         glacier function for destroy all kubernetes vaults
    """
    # Define connection
    glacier = boto3.client('glacier')

    # List all glacier vault
    glacier_vault_list = glacier_list_vaults()

    # Nuke all glacier vault
    for vault in glacier_vault_list:

        # Delete glacier vault
        glacier.delete_vault(vaultName=vault)
        logger.info("Nuke glacier vault %s", vault)


def glacier_list_vaults():
    """
       Aws glacier container service, list name of
       all glacier vault and return it in list.
    """

    # Define the connection
    glacier = boto3.client('glacier')
    paginator = glacier.get_paginator('list_vaults')
    page_iterator = paginator.paginate()

    # Initialize glacier vault list
    glacier_vault_list = []

    # Retrieve all glacier vault
    for page in page_iterator:
        for vault in page['VaultList']:

            glacier_vault = vault['VaultName']
            glacier_vault_list.insert(0, glacier_vault)

    return glacier_vault_list
