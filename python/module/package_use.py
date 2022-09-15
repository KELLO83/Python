import travel.th
th_temp=travel.th.Thpackage()
th_temp.detail()

import travel.vi

vi_temp=travel.vi.vipackage()

vi_temp.detail()

from travel.th import Thpackage

temp=Thpackage()

temp.detail()

from travel.vi import vipackage

temp_1=vipackage()

temp_1.detail()

from travel.th import Thpackage

temp_2=Thpackage()

temp_2.detail()

