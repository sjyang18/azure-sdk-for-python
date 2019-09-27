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

from .alert_rule import AlertRule


class MicrosoftSecurityIncidentCreationAlertRule(AlertRule):
    """Represents MicrosoftSecurityIncidentCreation rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param etag: Etag of the azure resource
    :type etag: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param display_names_filter: the alerts' displayNames on which the cases
     will be generated
    :type display_names_filter: list[str]
    :param product_filter: Required. The alerts' productName on which the
     cases will be generated. Possible values include: 'Microsoft Cloud App
     Security', 'Azure Security Center', 'Azure Advanced Threat Protection',
     'Azure Active Directory Identity Protection'
    :type product_filter: str or
     ~azure.mgmt.securityinsight.models.MicrosoftSecurityProductName
    :param severities_filter: the alerts' severities on which the cases will
     be generated
    :type severities_filter: list[str or
     ~azure.mgmt.securityinsight.models.AlertSeverity]
    :param alert_rule_template_name: The Name of the alert rule template used
     to create this rule.
    :type alert_rule_template_name: str
    :param description: The description of the alert rule.
    :type description: str
    :param display_name: Required. The display name for alerts created by this
     alert rule.
    :type display_name: str
    :param enabled: Required. Determines whether this alert rule is enabled or
     disabled.
    :type enabled: bool
    :ivar last_modified_utc: The last time that this alert has been modified.
    :vartype last_modified_utc: datetime
    :param tactics: The tactics of the alert rule
    :type tactics: list[str or
     ~azure.mgmt.securityinsight.models.AttackTactic]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'required': True},
        'product_filter': {'required': True},
        'display_name': {'required': True},
        'enabled': {'required': True},
        'last_modified_utc': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'display_names_filter': {'key': 'properties.displayNamesFilter', 'type': '[str]'},
        'product_filter': {'key': 'properties.productFilter', 'type': 'str'},
        'severities_filter': {'key': 'properties.severitiesFilter', 'type': '[str]'},
        'alert_rule_template_name': {'key': 'properties.alertRuleTemplateName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'last_modified_utc': {'key': 'properties.lastModifiedUtc', 'type': 'iso-8601'},
        'tactics': {'key': 'properties.tactics', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(MicrosoftSecurityIncidentCreationAlertRule, self).__init__(**kwargs)
        self.display_names_filter = kwargs.get('display_names_filter', None)
        self.product_filter = kwargs.get('product_filter', None)
        self.severities_filter = kwargs.get('severities_filter', None)
        self.alert_rule_template_name = kwargs.get('alert_rule_template_name', None)
        self.description = kwargs.get('description', None)
        self.display_name = kwargs.get('display_name', None)
        self.enabled = kwargs.get('enabled', None)
        self.last_modified_utc = None
        self.tactics = kwargs.get('tactics', None)
        self.kind = 'MicrosoftSecurityIncidentCreation'
