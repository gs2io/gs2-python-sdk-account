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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_account_client.Gs2Account import Gs2Account


class DeleteTakeOverRequest(Gs2UserRequest):

    class Constant(Gs2Account):
        FUNCTION = "DeleteTakeOver"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteTakeOverRequest, self).__init__(params)
        if params is None:
            self.__game_name = None
            self.__type = None
            self.__user_identifier = None
        else:
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)
            self.set_type(params['type'] if 'type' in params.keys() else None)
            self.set_user_identifier(params['userIdentifier'] if 'userIdentifier' in params.keys() else None)

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
        :rtype: DeleteTakeOverRequest
        """
        self.set_game_name(game_name)
        return self

    def get_user_identifier(self):
        """
        削除する引き継ぎ情報のユーザ固有IDを指定します。を取得
        :return: 削除する引き継ぎ情報のユーザ固有IDを指定します。
        :rtype: unicode
        """
        return self.__user_identifier

    def set_user_identifier(self, user_identifier):
        """
        削除する引き継ぎ情報のユーザ固有IDを指定します。を設定
        :param user_identifier: 削除する引き継ぎ情報のユーザ固有IDを指定します。
        :type user_identifier: unicode
        """
        if user_identifier is not None and not (isinstance(user_identifier, str) or isinstance(user_identifier, unicode)):
            raise TypeError(type(user_identifier))
        self.__user_identifier = user_identifier

    def with_user_identifier(self, user_identifier):
        """
        削除する引き継ぎ情報のユーザ固有IDを指定します。を設定
        :param user_identifier: 削除する引き継ぎ情報のユーザ固有IDを指定します。
        :type user_identifier: unicode
        :return: this
        :rtype: DeleteTakeOverRequest
        """
        self.set_user_identifier(user_identifier)
        return self

    def get_type(self):
        """
        削除する引き継ぎ情報の種類を指定します。を取得
        :return: 削除する引き継ぎ情報の種類を指定します。
        :rtype: int
        """
        return self.__type

    def set_type(self, _type):
        """
        削除する引き継ぎ情報の種類を指定します。を設定
        :param _type: 削除する引き継ぎ情報の種類を指定します。
        :type _type: int
        """
        if type is not None and not isinstance(type, int):
            raise TypeError(type(type))
        self.__type = type

    def with_type(self, _type):
        """
        削除する引き継ぎ情報の種類を指定します。を設定
        :param _type: 削除する引き継ぎ情報の種類を指定します。
        :type _type: int
        :return: this
        :rtype: DeleteTakeOverRequest
        """
        self.set_type(_type)
        return self
