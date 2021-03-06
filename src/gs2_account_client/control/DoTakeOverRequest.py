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


class DoTakeOverRequest(Gs2BasicRequest):

    class Constant(Gs2Account):
        FUNCTION = "DoTakeOver"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DoTakeOverRequest, self).__init__(params)
        if params is None:
            self.__game_name = None
        else:
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)
        if params is None:
            self.__type = None
        else:
            self.set_type(params['type'] if 'type' in params.keys() else None)
        if params is None:
            self.__user_identifier = None
        else:
            self.set_user_identifier(params['userIdentifier'] if 'userIdentifier' in params.keys() else None)
        if params is None:
            self.__password = None
        else:
            self.set_password(params['password'] if 'password' in params.keys() else None)

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
        if game_name is not None and not (isinstance(game_name, str) or isinstance(game_name, unicode)):
            raise TypeError(type(game_name))
        self.__game_name = game_name

    def with_game_name(self, game_name):
        """
        ゲームの名前を指定します。を設定
        :param game_name: ゲームの名前を指定します。
        :type game_name: unicode
        :return: this
        :rtype: DoTakeOverRequest
        """
        self.set_game_name(game_name)
        return self

    def get_user_identifier(self):
        """
        引き継ぎ情報のユーザ固有IDを取得
        :return: 引き継ぎ情報のユーザ固有ID
        :rtype: unicode
        """
        return self.__user_identifier

    def set_user_identifier(self, user_identifier):
        """
        引き継ぎ情報のユーザ固有IDを設定
        :param user_identifier: 引き継ぎ情報のユーザ固有ID
        :type user_identifier: unicode
        """
        if user_identifier is not None and not (isinstance(user_identifier, str) or isinstance(user_identifier, unicode)):
            raise TypeError(type(user_identifier))
        self.__user_identifier = user_identifier

    def with_user_identifier(self, user_identifier):
        """
        引き継ぎ情報のユーザ固有IDを設定
        :param user_identifier: 引き継ぎ情報のユーザ固有ID
        :type user_identifier: unicode
        :return: this
        :rtype: DoTakeOverRequest
        """
        self.set_user_identifier(user_identifier)
        return self

    def get_password(self):
        """
        引き継ぎ設定に指定されたパスワードを取得
        :return: 引き継ぎ設定に指定されたパスワード
        :rtype: unicode
        """
        return self.__password

    def set_password(self, password):
        """
        引き継ぎ設定に指定されたパスワードを設定
        :param password: 引き継ぎ設定に指定されたパスワード
        :type password: unicode
        """
        if password is not None and not (isinstance(password, str) or isinstance(password, unicode)):
            raise TypeError(type(password))
        self.__password = password

    def with_password(self, password):
        """
        引き継ぎ設定に指定されたパスワードを設定
        :param password: 引き継ぎ設定に指定されたパスワード
        :type password: unicode
        :return: this
        :rtype: DoTakeOverRequest
        """
        self.set_password(password)
        return self

    def get_type(self):
        """
        引き継ぎ情報の種類を指定します。を取得
        :return: 引き継ぎ情報の種類を指定します。
        :rtype: int
        """
        return self.__type

    def set_type(self, type_):
        """
        引き継ぎ情報の種類を指定します。を設定
        :param type_: 引き継ぎ情報の種類を指定します。
        :type type_: int
        """
        if type_ is not None and not isinstance(type_, int):
            raise TypeError(type(type_))
        self.__type = type_

    def with_type(self, type_):
        """
        引き継ぎ情報の種類を指定します。を設定
        :param type_: 引き継ぎ情報の種類を指定します。
        :type type_: int
        :return: this
        :rtype: DoTakeOverRequest
        """
        self.set_type(type_)
        return self
