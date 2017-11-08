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


class UpdateGameRequest(Gs2BasicRequest):

    class Constant(Gs2Account):
        FUNCTION = "UpdateGame"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateGameRequest, self).__init__(params)
        if params is None:
            self.__game_name = None
            self.__change_password_if_take_over = None
            self.__service_class = None
            self.__description = None
        else:
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)
            self.set_change_password_if_take_over(params['changePasswordIfTakeOver'] if 'changePasswordIfTakeOver' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)

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
        :rtype: UpdateGameRequest
        """
        self.set_game_name(game_name)
        return self

    def get_change_password_if_take_over(self):
        """
        引き継ぎ時にアカウントのパスワードを変更するかを取得
        :return: 引き継ぎ時にアカウントのパスワードを変更するか
        :rtype: bool
        """
        return self.__change_password_if_take_over

    def set_change_password_if_take_over(self, change_password_if_take_over):
        """
        引き継ぎ時にアカウントのパスワードを変更するかを設定
        :param change_password_if_take_over: 引き継ぎ時にアカウントのパスワードを変更するか
        :type change_password_if_take_over: bool
        """
        self.__change_password_if_take_over = change_password_if_take_over

    def with_change_password_if_take_over(self, change_password_if_take_over):
        """
        引き継ぎ時にアカウントのパスワードを変更するかを設定
        :param change_password_if_take_over: 引き継ぎ時にアカウントのパスワードを変更するか
        :type change_password_if_take_over: bool
        :return: this
        :rtype: UpdateGameRequest
        """
        self.set_change_password_if_take_over(change_password_if_take_over)
        return self

    def get_service_class(self):
        """
        ゲームのサービスクラスを取得
        :return: ゲームのサービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        ゲームのサービスクラスを設定
        :param service_class: ゲームのサービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

    def with_service_class(self, service_class):
        """
        ゲームのサービスクラスを設定
        :param service_class: ゲームのサービスクラス
        :type service_class: unicode
        :return: this
        :rtype: UpdateGameRequest
        """
        self.set_service_class(service_class)
        return self

    def get_description(self):
        """
        ゲームの説明を取得
        :return: ゲームの説明
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        ゲームの説明を設定
        :param description: ゲームの説明
        :type description: unicode
        """
        self.__description = description

    def with_description(self, description):
        """
        ゲームの説明を設定
        :param description: ゲームの説明
        :type description: unicode
        :return: this
        :rtype: UpdateGameRequest
        """
        self.set_description(description)
        return self
