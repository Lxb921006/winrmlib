# (c) 2015, Ian Clegg <ian.clegg@sourcewarp.com>
#
# winrmlib is licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
__title__ = 'winrmlib'
__author__ = 'ian.clegg@sourcewarp.com'
__license__ = 'Apache 2.0'


class AsHex:
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return ":".join([hex(ord(c))[2:].zfill(2) for c in self.s])
