## About the connector
This connector is providing automation actions for Anything LLM that supports using Retrieval Augmented Generation (RAG) with an LLM and user documents embedded in a vector DB. The LLM and vector DB can be fully local for maximum data privacy or configured to use cloud-based services such as OpenAI. A variety of LLMs and vector DBs are supported. Anything LLM itself can be installed on customer infrastructure or accessed as a cloud service.
<p>This document provides information about the Anything LLM Connector, which facilitates automated interactions, with a Anything LLM server using FortiSOAR&trade; playbooks. Add the Anything LLM Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Anything LLM.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-anything-llm</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Anything LLM server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Anything LLM server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Anything LLM</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL to which you will connect and perform the automated operations.
</td>
</tr><tr><td>API Key</td><td>Specify the API key to access the Anything LLM server.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Documents List</td><td>Retrieves a list of all document those are uploaded on server.</td><td>get_documents <br/>Investigation</td></tr>
<tr><td>Get Document by Name</td><td>Retrieves a document details by providing their name.</td><td>get_document <br/>Investigation</td></tr>
<tr><td>Get Workspace List</td><td>Retrieves a list of all current workspace present on AnythingLLM server.</td><td>get_workspace_list <br/>Investigation</td></tr>
<tr><td>Get Workspace by Slug</td><td>Retrieves a workspace details by providing Workspace Slug.</td><td>get_workspace <br/>Investigation</td></tr>
<tr><td>Add Workspace Embedding</td><td>Add a document to a workspace and create its vector embedding in the workspace.</td><td>add_workspace_embedding <br/>Investigation</td></tr>
<tr><td>Upload Document</td><td>Upload document on Anything LLM server.</td><td>upload_document <br/>Investigation</td></tr>
<tr><td>Upload Document Link</td><td>Uploads a web link to the custom-documents folder.</td><td>upload_document_link <br/>Investigation</td></tr>
<tr><td>Upload Document Text</td><td>Uploads a plain text to the custom-documents folder.</td><td>upload_document_text <br/>Investigation</td></tr>
<tr><td>Create Workspace</td><td>Create new workspace on AnythingLLM server.</td><td>create_workspace <br/>Investigation</td></tr>
<tr><td>Create Folder in Documents</td><td>Create a new folder inside the documents storage directory.</td><td>create_document_folder <br/>Investigation</td></tr>
<tr><td>Update Workspace Settings</td><td>Update workspace settings which present on AnythingLLM server.</td><td>update_workspace_settings <br/>Investigation</td></tr>
<tr><td>Workspace Chat</td><td>Send a chat message to a workspace (default thread). Query mode is based on embedded documents in chat, whereas chat mode is more general</td><td>workspace_chat <br/>Investigation</td></tr>
<tr><td>Move Document</td><td>Move document within the documents storage directory.</td><td>move_document <br/>Investigation</td></tr>
<tr><td>Delete Document</td><td>Delete document permanently from AnythingLLM server.</td><td>delete_document <br/>Investigation</td></tr>
<tr><td>Remove Workspace Embedding</td><td>Remove a document embedding from the workspace</td><td>delete_workspace_embedding <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Documents List
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "localFiles": {
        "name": "",
        "type": "",
        "items": [
            {
                "name": "",
                "type": "",
                "items": [
                    {
                        "id": "",
                        "url": "",
                        "name": "",
                        "type": "",
                        "title": "",
                        "cached": "",
                        "watched": "",
                        "canWatch": "",
                        "docAuthor": "",
                        "docSource": "",
                        "published": "",
                        "wordCount": "",
                        "chunkSource": "",
                        "description": "",
                        "pinnedWorkspaces": [],
                        "token_count_estimate": ""
                    }
                ]
            }
        ]
    }
}</pre>
### operation: Get Document by Name
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Document Name</td><td>Specify the document name to get document details.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "document": {
        "id": "",
        "url": "",
        "name": "",
        "type": "",
        "title": "",
        "cached": "",
        "docAuthor": "",
        "docSource": "",
        "published": "",
        "wordCount": "",
        "chunkSource": "",
        "description": "",
        "token_count_estimate": ""
    }
}</pre>
### operation: Get Workspace List
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "workspaces": [
        {
            "id": "",
            "name": "",
            "slug": "",
            "topN": "",
            "chatMode": "",
            "chatModel": "",
            "createdAt": "",
            "vectorTag": "",
            "agentModel": "",
            "openAiTemp": "",
            "pfpFilename": "",
            "chatProvider": "",
            "openAiPrompt": "",
            "agentProvider": "",
            "lastUpdatedAt": "",
            "openAiHistory": "",
            "similarityThreshold": "",
            "queryRefusalResponse": ""
        }
    ]
}</pre>
### operation: Get Workspace by Slug
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Workspace Slug</td><td>Specify the Workspace Slug to get workspace details.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": "",
    "workspace": {
        "id": "",
        "name": "",
        "slug": "",
        "topN": "",
        "chatMode": "",
        "chatModel": "",
        "createdAt": "",
        "vectorTag": "",
        "agentModel": "",
        "openAiTemp": "",
        "pfpFilename": "",
        "chatProvider": "",
        "openAiPrompt": "",
        "agentProvider": "",
        "lastUpdatedAt": "",
        "openAiHistory": "",
        "similarityThreshold": "",
        "queryRefusalResponse": ""
    }
}</pre>
### operation: Add Workspace Embedding
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Workspace Slug</td><td>Specify the Workspace Slug to embedding the document.
</td></tr><tr><td>Folder Name</td><td>Specify the folder name to add document from directory.
</td></tr><tr><td>Document Name</td><td>Specify the name of document to add embedding from provided directory.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "workspace": {
        "id": "",
        "name": "",
        "slug": "",
        "topN": "",
        "chatMode": "",
        "chatModel": "",
        "createdAt": "",
        "documents": [
            {
                "id": "",
                "docId": "",
                "pinned": "",
                "docpath": "",
                "watched": "",
                "filename": "",
                "metadata": "",
                "createdAt": "",
                "workspaceId": "",
                "lastUpdatedAt": ""
            }
        ],
        "vectorTag": "",
        "agentModel": "",
        "openAiTemp": "",
        "pfpFilename": "",
        "chatProvider": "",
        "openAiPrompt": "",
        "agentProvider": "",
        "lastUpdatedAt": "",
        "openAiHistory": "",
        "similarityThreshold": "",
        "queryRefusalResponse": ""
    }
}</pre>
### operation: Upload Document
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filepath or Record IRI</td><td>Filepath/Record IRI of the document file that you want to upload on Anything LLM server.
<br><strong>If you choose 'Filepath'</strong><ul><li>Filepath: Specify the file path on the filesystem. Note: Please set appropriate permissions to access input file.</li></ul><strong>If you choose 'Record IRI'</strong><ul><li>Record IRI: Specify the FortiSOAR™ IRI of the file. Note: The file that you want to upload on Anything LLM server must be part of the Attachment module in FortiSOAR™.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "success": "",
    "error": "",
    "documents": []
}</pre>
### operation: Upload Document Link
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Web Link</td><td>Specify the web link to upload on AnythingLLM server.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "success": "",
    "error": "",
    "documents": [
        {
            "id": "",
            "url": "",
            "title": "",
            "docAuthor": "",
            "description": "",
            "docSource": "",
            "chunkSource": "",
            "published": "",
            "wordCount": "",
            "pageContent": "",
            "token_count_estimate": "",
            "location": ""
        }
    ]
}</pre>
### operation: Upload Document Text
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Plain Text</td><td>Specify the raw text content that is the document.
</td></tr><tr><td>Document Title</td><td>Specify the document title to use when uploading.
</td></tr><tr><td>Description</td><td>Specify the description for the document.
</td></tr><tr><td>Author</td><td>Specify the author name for the document.
</td></tr><tr><td>Source</td><td>Specify the source name for the document.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "error": "",
    "success": "",
    "documents": [
        {
            "id": "",
            "url": "",
            "title": "",
            "location": "",
            "docAuthor": "",
            "docSource": "",
            "published": "",
            "wordCount": "",
            "chunkSource": "",
            "description": "",
            "pageContent": "",
            "token_count_estimate": ""
        }
    ]
}</pre>
### operation: Create Workspace
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Workspace Name</td><td>Specify the workspace name to create new workspace.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "workspace": {
        "id": "",
        "name": "",
        "slug": "",
        "createdAt": "",
        "openAiTemp": "",
        "lastUpdatedAt": "",
        "openAiHistory": "",
        "openAiPrompt": ""
    },
    "message": ""
}</pre>
### operation: Create Folder in Documents
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Folder Name</td><td>Specify the folder name to create into documents storage directory.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": "",
    "success": ""
}</pre>
### operation: Update Workspace Settings
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Workspace Slug</td><td>Specify the Workspace Slug to update workspace details.
</td></tr><tr><td>Workspace Settings</td><td>Specify the workspace settings to update workspace.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "workspace": {
        "id": "",
        "name": "",
        "slug": "",
        "createdAt": "",
        "openAiTemp": "",
        "lastUpdatedAt": "",
        "openAiHistory": "",
        "openAiPrompt": "",
        "documents": []
    },
    "message": ""
}</pre>
### operation: Workspace Chat
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Workspace Slug</td><td>Specify the Workspace Slug to chat with.
</td></tr><tr><td>Massage to send</td><td>Specify the massage to send on workspace.
</td></tr><tr><td>Mode</td><td>Specify the mode to chat, query or chat. Possible values are: query, chat.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "type": "",
    "close": "",
    "error": "",
    "chatId": "",
    "sources": [],
    "textResponse": ""
}</pre>
### operation: Move Document
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Source Folder Name</td><td>Specify the folder name to move file from directory.
</td></tr><tr><td>Destination Folder Name</td><td>Specify the folder name to move file to directory.
</td></tr><tr><td>Document Name</td><td>Specify the name of document to move from source directory to destination directory.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": "",
    "success": ""
}</pre>
### operation: Delete Document
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Folder Name</td><td>Specify the folder name to delete file from directory.
</td></tr><tr><td>Document Name</td><td>Specify the name of document to delete from directory.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "message": "",
    "success": ""
}</pre>
### operation: Remove Workspace Embedding
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Workspace Slug</td><td>Specify the Workspace Slug to remove a embedding the document.
</td></tr><tr><td>Folder Name</td><td>Specify the folder name to remove document from directory.
</td></tr><tr><td>Document Name</td><td>Specify the name of document to remove embedding from provided directory.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "workspace": {
        "id": "",
        "name": "",
        "slug": "",
        "topN": "",
        "chatMode": "",
        "chatModel": "",
        "createdAt": "",
        "documents": [
            {
                "id": "",
                "docId": "",
                "pinned": "",
                "docpath": "",
                "watched": "",
                "filename": "",
                "metadata": "",
                "createdAt": "",
                "workspaceId": "",
                "lastUpdatedAt": ""
            }
        ],
        "vectorTag": "",
        "agentModel": "",
        "openAiTemp": "",
        "pfpFilename": "",
        "chatProvider": "",
        "openAiPrompt": "",
        "agentProvider": "",
        "lastUpdatedAt": "",
        "openAiHistory": "",
        "similarityThreshold": "",
        "queryRefusalResponse": ""
    }
}</pre>
## Included playbooks
The `Sample - anything-llm - 1.0.0` playbook collection comes bundled with the Anything LLM connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Anything LLM connector.

- Add Workspace Embedding
- Create Folder in Documents
- Create Workspace
- Delete Document
- Get Document by Name
- Get Documents List
- Get Workspace List
- Get Workspace by Slug
- Move Document
- Remove Workspace Embedding
- Update Workspace Settings
- Upload Document
- Upload Document Link
- Upload Document Text
- Workspace Chat

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
