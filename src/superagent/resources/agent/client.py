# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.agent_list_output import AgentListOutput
from ...types.agent_output import AgentOutput
from ...types.http_validation_error import HttpValidationError
from ...types.predict_agent_output import PredictAgentOutput

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AgentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_agents(self) -> AgentListOutput:
        """
        List all agents
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/v1/agents"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentListOutput, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_agent(
        self,
        *,
        name: str,
        type: str,
        description: typing.Optional[str] = OMIT,
        avatar_url: typing.Optional[str] = OMIT,
        llm: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        has_memory: typing.Optional[bool] = OMIT,
        prompt_id: typing.Optional[str] = OMIT,
    ) -> AgentOutput:
        """
        Create a new agent

        Parameters:
            - name: str.

            - type: str.

            - description: typing.Optional[str].

            - avatar_url: typing.Optional[str].

            - llm: typing.Optional[typing.Dict[str, typing.Any]].

            - has_memory: typing.Optional[bool].

            - prompt_id: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {"name": name, "type": type}
        if description is not OMIT:
            _request["description"] = description
        if avatar_url is not OMIT:
            _request["avatarUrl"] = avatar_url
        if llm is not OMIT:
            _request["llm"] = llm
        if has_memory is not OMIT:
            _request["hasMemory"] = has_memory
        if prompt_id is not OMIT:
            _request["promptId"] = prompt_id
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/v1/agents"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_library_agents(self) -> AgentListOutput:
        """
        List all library agents
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/v1/agents/library"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentListOutput, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_agent(self, agent_id: str) -> AgentOutput:
        """
        Get a specific agent

        Parameters:
            - agent_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/v1/agents/{agent_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def patch_agent(self, agent_id: str, *, request: typing.Dict[str, typing.Any]) -> AgentOutput:
        """
        Patch a specific agent

        Parameters:
            - agent_id: str.

            - request: typing.Dict[str, typing.Any].
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/v1/agents/{agent_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_agent(self, agent_id: str) -> AgentOutput:
        """
        Delete a specific agent

        Parameters:
            - agent_id: str.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/v1/agents/{agent_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def prompt_agent(
        self,
        agent_id: str,
        *,
        input: typing.Dict[str, typing.Any],
        has_streaming: typing.Optional[bool] = OMIT,
        session: typing.Optional[str] = OMIT,
    ) -> PredictAgentOutput:
        """
        Invoke a specific agent

        Parameters:
            - agent_id: str.

            - input: typing.Dict[str, typing.Any].

            - has_streaming: typing.Optional[bool].

            - session: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {"input": input}
        if has_streaming is not OMIT:
            _request["has_streaming"] = has_streaming
        if session is not OMIT:
            _request["session"] = session
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/v1/agents/{agent_id}/predict"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PredictAgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAgentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_agents(self) -> AgentListOutput:
        """
        List all agents
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/v1/agents"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentListOutput, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_agent(
        self,
        *,
        name: str,
        type: str,
        description: typing.Optional[str] = OMIT,
        avatar_url: typing.Optional[str] = OMIT,
        llm: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        has_memory: typing.Optional[bool] = OMIT,
        prompt_id: typing.Optional[str] = OMIT,
    ) -> AgentOutput:
        """
        Create a new agent

        Parameters:
            - name: str.

            - type: str.

            - description: typing.Optional[str].

            - avatar_url: typing.Optional[str].

            - llm: typing.Optional[typing.Dict[str, typing.Any]].

            - has_memory: typing.Optional[bool].

            - prompt_id: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {"name": name, "type": type}
        if description is not OMIT:
            _request["description"] = description
        if avatar_url is not OMIT:
            _request["avatarUrl"] = avatar_url
        if llm is not OMIT:
            _request["llm"] = llm
        if has_memory is not OMIT:
            _request["hasMemory"] = has_memory
        if prompt_id is not OMIT:
            _request["promptId"] = prompt_id
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/v1/agents"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_library_agents(self) -> AgentListOutput:
        """
        List all library agents
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/v1/agents/library"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentListOutput, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_agent(self, agent_id: str) -> AgentOutput:
        """
        Get a specific agent

        Parameters:
            - agent_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/v1/agents/{agent_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def patch_agent(self, agent_id: str, *, request: typing.Dict[str, typing.Any]) -> AgentOutput:
        """
        Patch a specific agent

        Parameters:
            - agent_id: str.

            - request: typing.Dict[str, typing.Any].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/v1/agents/{agent_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_agent(self, agent_id: str) -> AgentOutput:
        """
        Delete a specific agent

        Parameters:
            - agent_id: str.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/v1/agents/{agent_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def prompt_agent(
        self,
        agent_id: str,
        *,
        input: typing.Dict[str, typing.Any],
        has_streaming: typing.Optional[bool] = OMIT,
        session: typing.Optional[str] = OMIT,
    ) -> PredictAgentOutput:
        """
        Invoke a specific agent

        Parameters:
            - agent_id: str.

            - input: typing.Dict[str, typing.Any].

            - has_streaming: typing.Optional[bool].

            - session: typing.Optional[str].
        """
        _request: typing.Dict[str, typing.Any] = {"input": input}
        if has_streaming is not OMIT:
            _request["has_streaming"] = has_streaming
        if session is not OMIT:
            _request["session"] = session
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/v1/agents/{agent_id}/predict"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PredictAgentOutput, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
