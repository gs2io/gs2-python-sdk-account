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

class Account(object):

    def __init__(self, params=None):
        if params is None:
            self.__user_id = None
            self.__password = None
            self.__create_at = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_password(params['password'] if 'password' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)


    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_password(self):
        """
        パスワードを取得
        :return: パスワード
        :rtype: unicode
        """
        return self.__password

    def set_password(self, password):
        """
        パスワードを設定
        :param password: パスワード
        :type password: unicode
        """
        self.__password = password

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

    def to_dict(self):
        return { 
            "userId": self.__user_id,
            "password": self.__password,
            "createAt": self.__create_at,
        }