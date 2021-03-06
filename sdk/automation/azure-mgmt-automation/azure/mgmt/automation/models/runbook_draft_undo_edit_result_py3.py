# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RunbookDraftUndoEditResult(Model):
    """The response model for the undo edit runbook operation.

    :param status_code: Possible values include: 'Continue',
     'SwitchingProtocols', 'OK', 'Created', 'Accepted',
     'NonAuthoritativeInformation', 'NoContent', 'ResetContent',
     'PartialContent', 'MultipleChoices', 'Ambiguous', 'MovedPermanently',
     'Moved', 'Found', 'Redirect', 'SeeOther', 'RedirectMethod', 'NotModified',
     'UseProxy', 'Unused', 'TemporaryRedirect', 'RedirectKeepVerb',
     'BadRequest', 'Unauthorized', 'PaymentRequired', 'Forbidden', 'NotFound',
     'MethodNotAllowed', 'NotAcceptable', 'ProxyAuthenticationRequired',
     'RequestTimeout', 'Conflict', 'Gone', 'LengthRequired',
     'PreconditionFailed', 'RequestEntityTooLarge', 'RequestUriTooLong',
     'UnsupportedMediaType', 'RequestedRangeNotSatisfiable',
     'ExpectationFailed', 'UpgradeRequired', 'InternalServerError',
     'NotImplemented', 'BadGateway', 'ServiceUnavailable', 'GatewayTimeout',
     'HttpVersionNotSupported'
    :type status_code: str or ~azure.mgmt.automation.models.HttpStatusCode
    :param request_id:
    :type request_id: str
    """

    _attribute_map = {
        'status_code': {'key': 'statusCode', 'type': 'str'},
        'request_id': {'key': 'requestId', 'type': 'str'},
    }

    def __init__(self, *, status_code=None, request_id: str=None, **kwargs) -> None:
        super(RunbookDraftUndoEditResult, self).__init__(**kwargs)
        self.status_code = status_code
        self.request_id = request_id
