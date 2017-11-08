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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_account_client.Gs2Account import Gs2Account


class AuthenticationRequest(Gs2BasicRequest):

    class Constant(Gs2Account):
        FUNCTION = "Authentication"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(AuthenticationRequest, self).__init__(params)
        if params is None:
            self.__game_name = None
            self.__user_id = None
            self.__password = None
            self.__key_name = None
        else:
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_password(params['password'] if 'password' in params.keys() else None)
            self.set_key_name(params['keyName'] if 'keyName' in params.keys() else None)

    def get_game_name(self):
        """
        ゲームの名前を指定します。を取得
        :return: ゲームの名前を指定します。
        :rtype: unicode
        """
        return self.__game_name

    def set_game_name(self, game_name):
        """
        ゲームの名前を指定します。を設定
        :param game_name: ゲームの名前を指定します。
        :type game_name: unicode
        """
        self.__game_name = game_name

    def with_game_name(self, game_name):
        """
        ゲームの名前を指定します。を設定
        :param game_name: ゲームの名前を指定します。
        :type game_name: unicode
        :return: this
        :rtype: AuthenticationRequest
        """
        self.set_game_name(game_name)
        return self

    def get_user_id(self):
        """
        認証する対象アカウントのユーザIDを指定します。を取得
        :return: 認証する対象アカウントのユーザIDを指定します。
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        認証する対象アカウントのユーザIDを指定します。を設定
        :param user_id: 認証する対象アカウントのユーザIDを指定します。
        :type user_id: unicode
        """
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        認証する対象アカウントのユーザIDを指定します。を設定
        :param user_id: 認証する対象アカウントのユーザIDを指定します。
        :type user_id: unicode
        :return: this
        :rtype: AuthenticationRequest
        """
        self.set_user_id(user_id)
        return self

    def get_password(self):
        """
        認証に利用するパスワードを取得
        :return: 認証に利用するパスワード
        :rtype: unicode
        """
        return self.__password

    def set_password(self, password):
        """
        認証に利用するパスワードを設定
        :param password: 認証に利用するパスワード
        :type password: unicode
        """
        self.__password = password

    def with_password(self, password):
        """
        認証に利用するパスワードを設定
        :param password: 認証に利用するパスワード
        :type password: unicode
        :return: this
        :rtype: AuthenticationRequest
        """
        self.set_password(password)
        return self

    def get_key_name(self):
        """
        認証結果の暗号化に利用する GS2-Key の暗号鍵名を取得
        :return: 認証結果の暗号化に利用する GS2-Key の暗号鍵名
        :rtype: unicode
        """
        return self.__key_name

    def set_key_name(self, key_name):
        """
        認証結果の暗号化に利用する GS2-Key の暗号鍵名を設定
        :param key_name: 認証結果の暗号化に利用する GS2-Key の暗号鍵名
        :type key_name: unicode
        """
        self.__key_name = key_name

    def with_key_name(self, key_name):
        """
        認証結果の暗号化に利用する GS2-Key の暗号鍵名を設定
        :param key_name: 認証結果の暗号化に利用する GS2-Key の暗号鍵名
        :type key_name: unicode
        :return: this
        :rtype: AuthenticationRequest
        """
        self.set_key_name(key_name)
        return self