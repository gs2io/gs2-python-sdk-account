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


class DeleteAccountRequest(Gs2BasicRequest):

    class Constant(Gs2Account):
        FUNCTION = "DeleteAccount"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteAccountRequest, self).__init__(params)
        if params is None:
            self.__game_name = None
            self.__user_id = None
        else:
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)

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
        :rtype: DeleteAccountRequest
        """
        self.set_game_name(game_name)
        return self

    def get_user_id(self):
        """
        削除する対象アカウントのユーザIDを指定します。を取得
        :return: 削除する対象アカウントのユーザIDを指定します。
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        削除する対象アカウントのユーザIDを指定します。を設定
        :param user_id: 削除する対象アカウントのユーザIDを指定します。
        :type user_id: unicode
        """
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        削除する対象アカウントのユーザIDを指定します。を設定
        :param user_id: 削除する対象アカウントのユーザIDを指定します。
        :type user_id: unicode
        :return: this
        :rtype: DeleteAccountRequest
        """
        self.set_user_id(user_id)
        return self