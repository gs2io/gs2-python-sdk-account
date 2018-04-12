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


class CreateGameRequest(Gs2BasicRequest):

    class Constant(Gs2Account):
        FUNCTION = "CreateGame"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateGameRequest, self).__init__(params)
        if params is None:
            self.__name = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__service_class = None
        else:
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
        if params is None:
            self.__change_password_if_take_over = None
        else:
            self.set_change_password_if_take_over(params['changePasswordIfTakeOver'] if 'changePasswordIfTakeOver' in params.keys() else None)
        if params is None:
            self.__create_account_trigger_script = None
        else:
            self.set_create_account_trigger_script(params['createAccountTriggerScript'] if 'createAccountTriggerScript' in params.keys() else None)
        if params is None:
            self.__create_account_done_trigger_script = None
        else:
            self.set_create_account_done_trigger_script(params['createAccountDoneTriggerScript'] if 'createAccountDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__authentication_trigger_script = None
        else:
            self.set_authentication_trigger_script(params['authenticationTriggerScript'] if 'authenticationTriggerScript' in params.keys() else None)
        if params is None:
            self.__authentication_done_trigger_script = None
        else:
            self.set_authentication_done_trigger_script(params['authenticationDoneTriggerScript'] if 'authenticationDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__create_take_over_trigger_script = None
        else:
            self.set_create_take_over_trigger_script(params['createTakeOverTriggerScript'] if 'createTakeOverTriggerScript' in params.keys() else None)
        if params is None:
            self.__create_take_over_done_trigger_script = None
        else:
            self.set_create_take_over_done_trigger_script(params['createTakeOverDoneTriggerScript'] if 'createTakeOverDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__do_take_over_trigger_script = None
        else:
            self.set_do_take_over_trigger_script(params['doTakeOverTriggerScript'] if 'doTakeOverTriggerScript' in params.keys() else None)
        if params is None:
            self.__do_take_over_done_trigger_script = None
        else:
            self.set_do_take_over_done_trigger_script(params['doTakeOverDoneTriggerScript'] if 'doTakeOverDoneTriggerScript' in params.keys() else None)

    def get_name(self):
        """
        ゲームの名前を取得
        :return: ゲームの名前
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        ゲームの名前を設定
        :param name: ゲームの名前
        :type name: unicode
        """
        if name and not isinstance(name, unicode):
            raise TypeError(type(name))
        self.__name = name

    def with_name(self, name):
        """
        ゲームの名前を設定
        :param name: ゲームの名前
        :type name: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_name(name)
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
        if description and not isinstance(description, unicode):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        ゲームの説明を設定
        :param description: ゲームの説明
        :type description: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_description(description)
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
        if service_class and not isinstance(service_class, unicode):
            raise TypeError(type(service_class))
        self.__service_class = service_class

    def with_service_class(self, service_class):
        """
        ゲームのサービスクラスを設定
        :param service_class: ゲームのサービスクラス
        :type service_class: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_service_class(service_class)
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
        if change_password_if_take_over and not isinstance(change_password_if_take_over, bool):
            raise TypeError(type(change_password_if_take_over))
        self.__change_password_if_take_over = change_password_if_take_over

    def with_change_password_if_take_over(self, change_password_if_take_over):
        """
        引き継ぎ時にアカウントのパスワードを変更するかを設定
        :param change_password_if_take_over: 引き継ぎ時にアカウントのパスワードを変更するか
        :type change_password_if_take_over: bool
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_change_password_if_take_over(change_password_if_take_over)
        return self

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
        if create_account_trigger_script and not isinstance(create_account_trigger_script, unicode):
            raise TypeError(type(create_account_trigger_script))
        self.__create_account_trigger_script = create_account_trigger_script

    def with_create_account_trigger_script(self, create_account_trigger_script):
        """
        アカウント新規作成時 に実行されるGS2-Scriptを設定
        :param create_account_trigger_script: アカウント新規作成時 に実行されるGS2-Script
        :type create_account_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_create_account_trigger_script(create_account_trigger_script)
        return self

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
        if create_account_done_trigger_script and not isinstance(create_account_done_trigger_script, unicode):
            raise TypeError(type(create_account_done_trigger_script))
        self.__create_account_done_trigger_script = create_account_done_trigger_script

    def with_create_account_done_trigger_script(self, create_account_done_trigger_script):
        """
        アカウント新規作成完了時 に実行されるGS2-Scriptを設定
        :param create_account_done_trigger_script: アカウント新規作成完了時 に実行されるGS2-Script
        :type create_account_done_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_create_account_done_trigger_script(create_account_done_trigger_script)
        return self

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
        if authentication_trigger_script and not isinstance(authentication_trigger_script, unicode):
            raise TypeError(type(authentication_trigger_script))
        self.__authentication_trigger_script = authentication_trigger_script

    def with_authentication_trigger_script(self, authentication_trigger_script):
        """
        認証時 に実行されるGS2-Scriptを設定
        :param authentication_trigger_script: 認証時 に実行されるGS2-Script
        :type authentication_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_authentication_trigger_script(authentication_trigger_script)
        return self

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
        if authentication_done_trigger_script and not isinstance(authentication_done_trigger_script, unicode):
            raise TypeError(type(authentication_done_trigger_script))
        self.__authentication_done_trigger_script = authentication_done_trigger_script

    def with_authentication_done_trigger_script(self, authentication_done_trigger_script):
        """
        認証完了時 に実行されるGS2-Scriptを設定
        :param authentication_done_trigger_script: 認証完了時 に実行されるGS2-Script
        :type authentication_done_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_authentication_done_trigger_script(authentication_done_trigger_script)
        return self

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
        if create_take_over_trigger_script and not isinstance(create_take_over_trigger_script, unicode):
            raise TypeError(type(create_take_over_trigger_script))
        self.__create_take_over_trigger_script = create_take_over_trigger_script

    def with_create_take_over_trigger_script(self, create_take_over_trigger_script):
        """
        引き継ぎ情報登録時 に実行されるGS2-Scriptを設定
        :param create_take_over_trigger_script: 引き継ぎ情報登録時 に実行されるGS2-Script
        :type create_take_over_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_create_take_over_trigger_script(create_take_over_trigger_script)
        return self

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
        if create_take_over_done_trigger_script and not isinstance(create_take_over_done_trigger_script, unicode):
            raise TypeError(type(create_take_over_done_trigger_script))
        self.__create_take_over_done_trigger_script = create_take_over_done_trigger_script

    def with_create_take_over_done_trigger_script(self, create_take_over_done_trigger_script):
        """
        引き継ぎ情報登録完了時 に実行されるGS2-Scriptを設定
        :param create_take_over_done_trigger_script: 引き継ぎ情報登録完了時 に実行されるGS2-Script
        :type create_take_over_done_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_create_take_over_done_trigger_script(create_take_over_done_trigger_script)
        return self

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
        if do_take_over_trigger_script and not isinstance(do_take_over_trigger_script, unicode):
            raise TypeError(type(do_take_over_trigger_script))
        self.__do_take_over_trigger_script = do_take_over_trigger_script

    def with_do_take_over_trigger_script(self, do_take_over_trigger_script):
        """
        引き継ぎ実行時 に実行されるGS2-Scriptを設定
        :param do_take_over_trigger_script: 引き継ぎ実行時 に実行されるGS2-Script
        :type do_take_over_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_do_take_over_trigger_script(do_take_over_trigger_script)
        return self

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
        if do_take_over_done_trigger_script and not isinstance(do_take_over_done_trigger_script, unicode):
            raise TypeError(type(do_take_over_done_trigger_script))
        self.__do_take_over_done_trigger_script = do_take_over_done_trigger_script

    def with_do_take_over_done_trigger_script(self, do_take_over_done_trigger_script):
        """
        引き継ぎ実行完了時 に実行されるGS2-Scriptを設定
        :param do_take_over_done_trigger_script: 引き継ぎ実行完了時 に実行されるGS2-Script
        :type do_take_over_done_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_do_take_over_done_trigger_script(do_take_over_done_trigger_script)
        return self
