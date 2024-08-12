"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from connectors.core.connector import ConnectorError, get_logger
import requests, os
from os.path import join
from connectors.cyops_utilities.builtins import upload_file_to_cyops, download_file_from_cyops, \
    extract_email_metadata_new

logger = get_logger('anything-llm')


def make_api_call(method="GET", endpoint="", config=None, data=None, header=None, files=None, json_data=None,
                  params=None, verify_ssl=False):
    try:
        headers = {"Authorization": "Bearer " + config.get("api_key")}
        if header:
            headers.update(header)
        url = config.get("server_url") + endpoint
        if json_data is None:
            response = requests.request(method=method, url=url, headers=headers, data=data, params=params, files=files,
                                        verify=verify_ssl)
        else:
            response = requests.request(method=method, url=url, headers=headers, data=data, json=json_data, files=files,
                                        params=params, verify=verify_ssl)
        if response.ok:
            if response.content:
                response = response.json()
            else:
                response = {{"result": "No Data Returned", "status": "success"}}
            return response
        else:
            logger.error("Error: {0}".format(response.json()))
            raise ConnectorError('{0}:{1}'.format(response.status_code, response.text))
    except requests.exceptions.SSLError as e:
        logger.exception('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
    except requests.exceptions.ConnectionError as e:
        logger.exception('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))


def get_documents(config, params):
    try:
        endpoint = "/api/v1/documents"
        return make_api_call(endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def get_document(config, params):
    try:
        endpoint = "/api/v1/document/" + params.get("doc_name")
        return make_api_call(endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def create_document_folder(config, params):
    try:
        endpoint = "/api/v1/document/create-folder"
        header = {"Content-Type": "application/json"}
        data = {
            "name": params.get("folder_name")
        }
        return make_api_call(method="POST", header=header, json_data=data, endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def move_document(config, params):
    try:
        endpoint = "/api/v1/document/move-files"
        header = {"Content-Type": "application/json"}
        data = {
            "files": [
                {
                    "from": params.get("src_folder_name", "") + "/" + params.get("doc_name", ""),
                    "to": params.get("dest_folder_name", "") + "/" + params.get("doc_name", "")
                }
            ]
        }
        return make_api_call(method="POST", header=header, json_data=data, endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def delete_document(config, params):
    try:
        endpoint = "/api/v1/system/remove-documents"
        header = {"Content-Type": "application/json"}
        data = {
            "names": [
                params.get("folder_name", "") + "/" + params.get("doc_name", "")
            ]
        }
        return make_api_call(method="DELETE", header=header, json_data=data, endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def get_workspace_list(config, params):
    try:
        endpoint = "/api/v1/workspaces"
        return make_api_call(endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def get_workspace(config, params):
    try:
        endpoint = "/api/v1/workspace/" + params.get("workspace_name")
        return make_api_call(endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def update_workspace_settings(config, params):
    try:
        endpoint = "/api/v1/workspace/" + params.get("workspace_name") + "/update"
        header = {"Content-Type": "application/json"}
        data = params.get("settings_data")
        return make_api_call(method="POST", header=header, json_data=data, endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def update_workspace_embedding(config, params, action):
    try:
        endpoint = "/api/v1/workspace/" + params.get("workspace_name") + "/update-embeddings"
        header = {"Content-Type": "application/json"}
        data = {}
        if action == "add":
            data.update({"adds": [
                params.get("folder_name", "") + "/" + params.get("doc_name", "")
            ]})
        else:
            data.update({"deletes": [
                params.get("folder_name", "") + "/" + params.get("doc_name", "")
            ]})
        return make_api_call(method="POST", header=header, json_data=data, endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def add_workspace_embedding(config, params):
    return update_workspace_embedding(config, params, "add")


def delete_workspace_embedding(config, params):
    return update_workspace_embedding(config, params, "delete")


def _workspace_chat(config, params, endpoint):
    try:
        endpoint = f'/api/v1/workspace/{params.get("workspace_name")}/' + endpoint
        header = {"Content-Type": "application/json"}
        data = {
            "message": params.get("message"),
            "mode": params.get("mode").lower()
        }
        return make_api_call(method="POST", header=header, json_data=data, endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def workspace_chat(config, params):
    return _workspace_chat(config, params, 'chat')


def workspace_stream_chat(config, params):
    return _workspace_chat(config, params, 'stream-chat')


def upload_document_link(config, params):
    try:
        endpoint = f'/api/v1/document/upload-link'
        header = {"Content-Type": "application/json"}
        data = {
            "link": params.get("web_link")
        }
        return make_api_call(method="POST", header=header, json_data=data, endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def upload_document_text(config, params):
    try:
        endpoint = f'/api/v1/document/raw-text'
        header = {"Content-Type": "application/json"}
        data = {
            "textContent": params.get("plain_text"),
            "metadata": {
                "title": params.get("doc_title"),
                "docAuthor": params.get("author"),
                "description": params.get("description"),
                "docSource": params.get("source")
            }
        }
        return make_api_call(method="POST", header=header, json_data=data, endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def create_workspace(config, params):
    try:
        endpoint = f'/api/v1/workspace/new'
        header = {"Content-Type": "application/json"}
        data = {
            "name": params.get("workspace_name")
        }
        return make_api_call(method="POST", header=header, json_data=data, endpoint=endpoint, config=config)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def upload_document(config, params):
    try:
        endpoint = "/api/v1/document/upload"
        file_type = params.get('file_type')
        file_iri = params.get('iri')
        file_name = params.get('file_name')
        if file_type == "Record IRI":
            file_download_response = download_file_from_cyops(file_iri)
            file_path = join('/tmp', file_download_response['cyops_file_path'])
            file_name = file_download_response['filename']
        else:
            if not os.path.exists(file_name):
                raise ConnectorError("File path not exist. Provided file path is: " + file_name)
            file_path = file_name
        file_name = file_name.split(os.sep)[-1]
        file = {'file': (
        file_name, open(file_path, 'rb'), 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')}
        return make_api_call(method="POST", endpoint=endpoint, config=config, files=file)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def check_health(config):
    try:
        endpoint = "/api/v1/auth"
        ret = make_api_call(endpoint=endpoint, config=config)
        return ret.get("authenticated", False)
    except Exception as err:
        logger.exception('Check Health Failed: {}'.format(str(err)))
        raise ConnectorError('Check Health Failed: {}'.format(str(err)))


operations_map = {
    'check_health': check_health,
    'get_documents': get_documents,
    'get_document': get_document,
    'create_document_folder': create_document_folder,
    'move_document': move_document,
    'delete_document': delete_document,
    'get_workspace_list': get_workspace_list,
    'get_workspace': get_workspace,
    'update_workspace_settings': update_workspace_settings,
    'add_workspace_embedding': add_workspace_embedding,
    'delete_workspace_embedding': delete_workspace_embedding,
    'workspace_chat': workspace_chat,
    'workspace_stream_chat': workspace_stream_chat,
    'upload_document': upload_document,
    'upload_document_link': upload_document_link,
    'upload_document_text': upload_document_text,
    'create_workspace': create_workspace
}
