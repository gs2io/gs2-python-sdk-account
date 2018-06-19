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
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__service_class = None
            self.__change_password_if_take_over = None
            self.__create_account_trigger_script = None
            self.__create_account_done_trigger_script = None
            self.__authentication_trigger_script = None
            self.__authentication_done_trigger_script = None
            self.__create_take_over_trigger_script = None
            self.__create_take_over_done_trigger_script = None
            self.__do_take_over_trigger_script = None
            self.__do_take_over_done_trigger_script = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_game_id(params['gameId'] if 'gameId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_change_password_if_take_over(params['changePasswordIfTakeOver'] if 'changePasswordIfTakeOver' in params.keys() else None)
            self.set_create_account_trigger_script(params['createAccountTriggerScript'] if 'createAccountTriggerScript' in params.keys() else None)
            self.set_create_account_done_trigger_script(params['createAccountDoneTriggerScript'] if 'createAccountDoneTriggerScript' in params.keys() else None)
            self.set_authentication_trigger_script(params['authenticationTriggerScript'] if 'authenticationTriggerScript' in params.keys() else None)
            self.set_authentication_done_trigger_script(params['authenticationDoneTriggerScript'] if 'authenticationDoneTriggerScript' in params.keys() else None)
            self.set_create_take_over_trigger_script(params['createTakeOverTriggerScript'] if 'createTakeOverTriggerScript' in params.keys() else None)
            self.set_create_take_over_done_trigger_script(params['createTakeOverDoneTriggerScript'] if 'createTakeOverDoneTriggerScript' in params.keys() else None)
            self.set_do_take_over_trigger_script(params['doTakeOverTriggerScript'] if 'doTakeOverTriggerScript' in params.keys() else None)
            self.set_do_take_over_done_trigger_script(params['doTakeOverDoneTriggerScript'] if 'doTakeOverDoneTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

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

    def get_create_account_trigger_script(self):
        """
        アカウント新規作成時 に実行されるGS2-Scriptを取得
        :return: アカウント新規作成時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_account_trigger_script

    def set_create_account_trigger_script(self, create_account_trigger_script):
        """
        アカウント新規作成時 に実行されるGS2-Scriptを設定
        :param create_account_trigger_script: アカウント新規作成時 に実行されるGS2-Script
        :type create_account_trigger_script: unicode
        """
        self.__create_account_trigger_script = create_account_trigger_script

    def get_create_account_done_trigger_script(self):
        """
        アカウント新規作成完了時 に実行されるGS2-Scriptを取得
        :return: アカウント新規作成完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_account_done_trigger_script

    def set_create_account_done_trigger_script(self, create_account_done_trigger_script):
        """
        アカウント新規作成完了時 に実行されるGS2-Scriptを設定
        :param create_account_done_trigger_script: アカウント新規作成完了時 に実行されるGS2-Script
        :type create_account_done_trigger_script: unicode
        """
        self.__create_account_done_trigger_script = create_account_done_trigger_script

    def get_authentication_trigger_script(self):
        """
        認証時 に実行されるGS2-Scriptを取得
        :return: 認証時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__authentication_trigger_script

    def set_authentication_trigger_script(self, authentication_trigger_script):
        """
        認証時 に実行されるGS2-Scriptを設定
        :param authentication_trigger_script: 認証時 に実行されるGS2-Script
        :type authentication_trigger_script: unicode
        """
        self.__authentication_trigger_script = authentication_trigger_script

    def get_authentication_done_trigger_script(self):
        """
        認証完了時 に実行されるGS2-Scriptを取得
        :return: 認証完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__authentication_done_trigger_script

    def set_authentication_done_trigger_script(self, authentication_done_trigger_script):
        """
        認証完了時 に実行されるGS2-Scriptを設定
        :param authentication_done_trigger_script: 認証完了時 に実行されるGS2-Script
        :type authentication_done_trigger_script: unicode
        """
        self.__authentication_done_trigger_script = authentication_done_trigger_script

    def get_create_take_over_trigger_script(self):
        """
        引き継ぎ情報登録時 に実行されるGS2-Scriptを取得
        :return: 引き継ぎ情報登録時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_take_over_trigger_script

    def set_create_take_over_trigger_script(self, create_take_over_trigger_script):
        """
        引き継ぎ情報登録時 に実行されるGS2-Scriptを設定
        :param create_take_over_trigger_script: 引き継ぎ情報登録時 に実行されるGS2-Script
        :type create_take_over_trigger_script: unicode
        """
        self.__create_take_over_trigger_script = create_take_over_trigger_script

    def get_create_take_over_done_trigger_script(self):
        """
        引き継ぎ情報登録完了時 に実行されるGS2-Scriptを取得
        :return: 引き継ぎ情報登録完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_take_over_done_trigger_script

    def set_create_take_over_done_trigger_script(self, create_take_over_done_trigger_script):
        """
        引き継ぎ情報登録完了時 に実行されるGS2-Scriptを設定
        :param create_take_over_done_trigger_script: 引き継ぎ情報登録完了時 に実行されるGS2-Script
        :type create_take_over_done_trigger_script: unicode
        """
        self.__create_take_over_done_trigger_script = create_take_over_done_trigger_script

    def get_do_take_over_trigger_script(self):
        """
        引き継ぎ実行時 に実行されるGS2-Scriptを取得
        :return: 引き継ぎ実行時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__do_take_over_trigger_script

    def set_do_take_over_trigger_script(self, do_take_over_trigger_script):
        """
        引き継ぎ実行時 に実行されるGS2-Scriptを設定
        :param do_take_over_trigger_script: 引き継ぎ実行時 に実行されるGS2-Script
        :type do_take_over_trigger_script: unicode
        """
        self.__do_take_over_trigger_script = do_take_over_trigger_script

    def get_do_take_over_done_trigger_script(self):
        """
        引き継ぎ実行完了時 に実行されるGS2-Scriptを取得
        :return: 引き継ぎ実行完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__do_take_over_done_trigger_script

    def set_do_take_over_done_trigger_script(self, do_take_over_done_trigger_script):
        """
        引き継ぎ実行完了時 に実行されるGS2-Scriptを設定
        :param do_take_over_done_trigger_script: 引き継ぎ実行完了時 に実行されるGS2-Script
        :type do_take_over_done_trigger_script: unicode
        """
        self.__do_take_over_done_trigger_script = do_take_over_done_trigger_script

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

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(Game, self).__getitem__(key)

    def to_dict(self):
        return {
            "gameId": self.__game_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "serviceClass": self.__service_class,
            "changePasswordIfTakeOver": self.__change_password_if_take_over,
            "createAccountTriggerScript": self.__create_account_trigger_script,
            "createAccountDoneTriggerScript": self.__create_account_done_trigger_script,
            "authenticationTriggerScript": self.__authentication_trigger_script,
            "authenticationDoneTriggerScript": self.__authentication_done_trigger_script,
            "createTakeOverTriggerScript": self.__create_take_over_trigger_script,
            "createTakeOverDoneTriggerScript": self.__create_take_over_done_trigger_script,
            "doTakeOverTriggerScript": self.__do_take_over_trigger_script,
            "doTakeOverDoneTriggerScript": self.__do_take_over_done_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
