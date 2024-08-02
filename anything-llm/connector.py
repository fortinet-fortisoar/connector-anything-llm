""" Copyright start
  Copyright (C) 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import operations_map
logger = get_logger('connector_anything-llm')


class AnythingLLM(Connector):
    def execute(self, config, operation, params, **kwargs):
        action = operations_map.get(operation)
        return action(config, params)

    def check_health(self, config):
        try:
            return operations_map.get("check_health")(config)
        except Exception as exp:
            logger.exception(str(exp))
            raise ConnectorError(str(exp))
