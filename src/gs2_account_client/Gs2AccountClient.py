# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2AccountClient(AbstractGs2Client):

    ENDPOINT = "account"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2AccountClient, self).__init__(credential, region)


    def authentication(self, request):
        """
        認証処理を行います<br>
        <br>
        - 消費クオータ: 3<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.AuthenticationRequest.AuthenticationRequest
        :return: 結果
        :rtype: gs2_account_client.control.AuthenticationResult.AuthenticationResult
        """
        body = { 
            "password": request.get_password(),
            "keyName": request.get_key_name(),
        }

        headers = { 
        }
        from gs2_account_client.control.AuthenticationRequest import AuthenticationRequest

        from gs2_account_client.control.AuthenticationResult import AuthenticationResult
        return AuthenticationResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/account/" + str(("null" if request.get_user_id() is None else request.get_user_id())) + "",
            service=self.ENDPOINT,
            module=AuthenticationRequest.Constant.MODULE,
            function=AuthenticationRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_account(self, request):
        """
        アカウントを登録します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.CreateAccountRequest.CreateAccountRequest
        :return: 結果
        :rtype: gs2_account_client.control.CreateAccountResult.CreateAccountResult
        """
        body = { 
        }

        headers = { 
        }
        from gs2_account_client.control.CreateAccountRequest import CreateAccountRequest

        from gs2_account_client.control.CreateAccountResult import CreateAccountResult
        return CreateAccountResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/account",
            service=self.ENDPOINT,
            module=CreateAccountRequest.Constant.MODULE,
            function=CreateAccountRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_game(self, request):
        """
        ゲームを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.CreateGameRequest.CreateGameRequest
        :return: 結果
        :rtype: gs2_account_client.control.CreateGameResult.CreateGameResult
        """
        body = { 
            "changePasswordIfTakeOver": request.get_change_password_if_take_over(),
            "serviceClass": request.get_service_class(),
            "name": request.get_name(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        from gs2_account_client.control.CreateGameRequest import CreateGameRequest

        from gs2_account_client.control.CreateGameResult import CreateGameResult
        return CreateGameResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game",
            service=self.ENDPOINT,
            module=CreateGameRequest.Constant.MODULE,
            function=CreateGameRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_take_over(self, request):
        """
        引き継ぎ情報を登録します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.CreateTakeOverRequest.CreateTakeOverRequest
        :return: 結果
        :rtype: gs2_account_client.control.CreateTakeOverResult.CreateTakeOverResult
        """
        body = { 
            "password": request.get_password(),
            "type": request.get_type(),
            "userIdentifier": request.get_user_identifier(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_account_client.control.CreateTakeOverRequest import CreateTakeOverRequest

        from gs2_account_client.control.CreateTakeOverResult import CreateTakeOverResult
        return CreateTakeOverResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/takeover",
            service=self.ENDPOINT,
            module=CreateTakeOverRequest.Constant.MODULE,
            function=CreateTakeOverRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def delete_account(self, request):
        """
        アカウントを削除します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.DeleteAccountRequest.DeleteAccountRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_account_client.control.DeleteAccountRequest import DeleteAccountRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/account/" + str(("null" if request.get_user_id() is None else request.get_user_id())) + "",
            service=self.ENDPOINT,
            module=DeleteAccountRequest.Constant.MODULE,
            function=DeleteAccountRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_game(self, request):
        """
        ゲームを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.DeleteGameRequest.DeleteGameRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_account_client.control.DeleteGameRequest import DeleteGameRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "",
            service=self.ENDPOINT,
            module=DeleteGameRequest.Constant.MODULE,
            function=DeleteGameRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_take_over(self, request):
        """
        引き継ぎ情報を削除します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.DeleteTakeOverRequest.DeleteTakeOverRequest

        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_account_client.control.DeleteTakeOverRequest import DeleteTakeOverRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/takeover/" + str(("null" if request.get_type() is None else request.get_type())) + "/" + str(("null" if request.get_user_identifier() is None else request.get_user_identifier())) + "",
            service=self.ENDPOINT,
            module=DeleteTakeOverRequest.Constant.MODULE,
            function=DeleteTakeOverRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def describe_account(self, request):
        """
        アカウントを取得します<br>
        <br>
        - 消費クオータ: 50件あたり5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.DescribeAccountRequest.DescribeAccountRequest
        :return: 結果
        :rtype: gs2_account_client.control.DescribeAccountResult.DescribeAccountResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_account_client.control.DescribeAccountRequest import DescribeAccountRequest

        from gs2_account_client.control.DescribeAccountResult import DescribeAccountResult
        return DescribeAccountResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/account",
            service=self.ENDPOINT,
            module=DescribeAccountRequest.Constant.MODULE,
            function=DescribeAccountRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_game(self, request):
        """
        ゲームの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.DescribeGameRequest.DescribeGameRequest
        :return: 結果
        :rtype: gs2_account_client.control.DescribeGameResult.DescribeGameResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_account_client.control.DescribeGameRequest import DescribeGameRequest

        from gs2_account_client.control.DescribeGameResult import DescribeGameResult
        return DescribeGameResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game",
            service=self.ENDPOINT,
            module=DescribeGameRequest.Constant.MODULE,
            function=DescribeGameRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_service_class(self, request):
        """
        サービスクラスの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.DescribeServiceClassRequest.DescribeServiceClassRequest
        :return: 結果
        :rtype: gs2_account_client.control.DescribeServiceClassResult.DescribeServiceClassResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_account_client.control.DescribeServiceClassRequest import DescribeServiceClassRequest

        from gs2_account_client.control.DescribeServiceClassResult import DescribeServiceClassResult
        return DescribeServiceClassResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/serviceClass",
            service=self.ENDPOINT,
            module=DescribeServiceClassRequest.Constant.MODULE,
            function=DescribeServiceClassRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_take_over(self, request):
        """
        引き継ぎ情報を取得します<br>
        <br>
        - 消費クオータ: 50件あたり5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.DescribeTakeOverRequest.DescribeTakeOverRequest
        :return: 結果
        :rtype: gs2_account_client.control.DescribeTakeOverResult.DescribeTakeOverResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_account_client.control.DescribeTakeOverRequest import DescribeTakeOverRequest

        from gs2_account_client.control.DescribeTakeOverResult import DescribeTakeOverResult
        return DescribeTakeOverResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/takeover",
            service=self.ENDPOINT,
            module=DescribeTakeOverRequest.Constant.MODULE,
            function=DescribeTakeOverRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))




    def do_take_over(self, request):
        """
        引き継ぎを実行します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.DoTakeOverRequest.DoTakeOverRequest
        :return: 結果
        :rtype: gs2_account_client.control.DoTakeOverResult.DoTakeOverResult
        """
        body = { 
            "password": request.get_password(),
            "userIdentifier": request.get_user_identifier(),
        }

        headers = { 
        }
        from gs2_account_client.control.DoTakeOverRequest import DoTakeOverRequest

        from gs2_account_client.control.DoTakeOverResult import DoTakeOverResult
        return DoTakeOverResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/takeover/" + str(("null" if request.get_type() is None else request.get_type())) + "",
            service=self.ENDPOINT,
            module=DoTakeOverRequest.Constant.MODULE,
            function=DoTakeOverRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def get_game(self, request):
        """
        ゲームを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.GetGameRequest.GetGameRequest
        :return: 結果
        :rtype: gs2_account_client.control.GetGameResult.GetGameResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_account_client.control.GetGameRequest import GetGameRequest

        from gs2_account_client.control.GetGameResult import GetGameResult
        return GetGameResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "",
            service=self.ENDPOINT,
            module=GetGameRequest.Constant.MODULE,
            function=GetGameRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_game_status(self, request):
        """
        ゲームのステータスを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.GetGameStatusRequest.GetGameStatusRequest
        :return: 結果
        :rtype: gs2_account_client.control.GetGameStatusResult.GetGameStatusResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_account_client.control.GetGameStatusRequest import GetGameStatusRequest

        from gs2_account_client.control.GetGameStatusResult import GetGameStatusResult
        return GetGameStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/status",
            service=self.ENDPOINT,
            module=GetGameStatusRequest.Constant.MODULE,
            function=GetGameStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_take_over(self, request):
        """
        引き継ぎ情報を取得します<br>
        <br>
        - 消費クオータ: 5<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.GetTakeOverRequest.GetTakeOverRequest
        :return: 結果
        :rtype: gs2_account_client.control.GetTakeOverResult.GetTakeOverResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_account_client.control.GetTakeOverRequest import GetTakeOverRequest

        from gs2_account_client.control.GetTakeOverResult import GetTakeOverResult
        return GetTakeOverResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/takeover/" + str(("null" if request.get_type() is None else request.get_type())) + "/" + str(("null" if request.get_user_identifier() is None else request.get_user_identifier())) + "",
            service=self.ENDPOINT,
            module=GetTakeOverRequest.Constant.MODULE,
            function=GetTakeOverRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def update_game(self, request):
        """
        ゲームを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.UpdateGameRequest.UpdateGameRequest
        :return: 結果
        :rtype: gs2_account_client.control.UpdateGameResult.UpdateGameResult
        """
        body = { 
            "changePasswordIfTakeOver": request.get_change_password_if_take_over(),
            "serviceClass": request.get_service_class(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        from gs2_account_client.control.UpdateGameRequest import UpdateGameRequest

        from gs2_account_client.control.UpdateGameResult import UpdateGameResult
        return UpdateGameResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "",
            service=self.ENDPOINT,
            module=UpdateGameRequest.Constant.MODULE,
            function=UpdateGameRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def update_take_over(self, request):
        """
        引き継ぎ情報を更新します<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_account_client.control.UpdateTakeOverRequest.UpdateTakeOverRequest
        :return: 結果
        :rtype: gs2_account_client.control.UpdateTakeOverResult.UpdateTakeOverResult
        """
        body = { 
            "password": request.get_password(),
            "oldPassword": request.get_old_password(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_account_client.control.UpdateTakeOverRequest import UpdateTakeOverRequest

        from gs2_account_client.control.UpdateTakeOverResult import UpdateTakeOverResult
        return UpdateTakeOverResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/takeover/" + str(("null" if request.get_type() is None else request.get_type())) + "/" + str(("null" if request.get_user_identifier() is None else request.get_user_identifier())) + "",
            service=self.ENDPOINT,
            module=UpdateTakeOverRequest.Constant.MODULE,
            function=UpdateTakeOverRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

