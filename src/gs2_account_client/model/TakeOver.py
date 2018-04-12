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


class TakeOver(object):

    def __init__(self, params=None):
        if params is None:
            self.__user_id = None
            self.__type = None
            self.__user_identifier = None
            self.__create_at = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_type(params['type'] if 'type' in params.keys() else None)
            self.set_user_identifier(params['userIdentifier'] if 'userIdentifier' in params.keys() else None)
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

    def get_user_identifier(self):
        """
        ユーザ識別子を取得
        :return: ユーザ識別子
        :rtype: unicode
        """
        return self.__user_identifier

    def set_user_identifier(self, user_identifier):
        """
        ユーザ識別子を設定
        :param user_identifier: ユーザ識別子
        :type user_identifier: unicode
        """
        self.__user_identifier = user_identifier

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

    def get_type(self):
        """
        アカウント種別を取得
        :return: アカウント種別
        :rtype: int
        """
        return self.__type

    def set_type(self, _type):
        """
        アカウント種別を設定
        :param _type: アカウント種別
        :type _type: int
        """
        self.__type = _type

    def to_dict(self):
        return {
            "userId": self.__user_id,
            "type": self.__type,
            "userIdentifier": self.__user_identifier,
            "createAt": self.__create_at,
        }
