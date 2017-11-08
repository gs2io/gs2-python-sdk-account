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

class Game(object):

    def __init__(self, params=None):
        if params is None:
            self.__game_id = None
            self.__name = None
            self.__service_class = None
            self.__create_at = None
            self.__owner_id = None
            self.__change_password_if_take_over = None
            self.__update_at = None
            self.__description = None
        else:
            self.set_game_id(params['gameId'] if 'gameId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_change_password_if_take_over(params['changePasswordIfTakeOver'] if 'changePasswordIfTakeOver' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)


    def get_game_id(self):
        """
        ゲームGRNを取得
        :return: ゲームGRN
        :rtype: unicode
        """
        return self.__game_id

    def set_game_id(self, game_id):
        """
        ゲームGRNを設定
        :param game_id: ゲームGRN
        :type game_id: unicode
        """
        self.__game_id = game_id

    def get_name(self):
        """
        ゲーム名を取得
        :return: ゲーム名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        ゲーム名を設定
        :param name: ゲーム名
        :type name: unicode
        """
        self.__name = name

    def get_service_class(self):
        """
        サービスクラスを取得
        :return: サービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_change_password_if_take_over(self):
        """
        アカウント引き継ぎ時にパスワードを変更するかを取得
        :return: アカウント引き継ぎ時にパスワードを変更するか
        :rtype: bool
        """
        return self.__change_password_if_take_over

    def set_change_password_if_take_over(self, change_password_if_take_over):
        """
        アカウント引き継ぎ時にパスワードを変更するかを設定
        :param change_password_if_take_over: アカウント引き継ぎ時にパスワードを変更するか
        :type change_password_if_take_over: bool
        """
        self.__change_password_if_take_over = change_password_if_take_over

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def to_dict(self):
        return { 
            "gameId": self.__game_id,
            "name": self.__name,
            "serviceClass": self.__service_class,
            "createAt": self.__create_at,
            "ownerId": self.__owner_id,
            "changePasswordIfTakeOver": self.__change_password_if_take_over,
            "updateAt": self.__update_at,
            "description": self.__description,
        }