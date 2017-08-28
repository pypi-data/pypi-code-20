# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = ("{{last_name}}{{first_name}}", )
    first_names = ('雅萍', '惠雯', '嘉玲', '宇軒', '雅文', '詩婷', '欣怡', '庭瑋',
                   '志偉', '怡萱', '美玲', '淑玲', '冠廷', '怡伶', '彥廷', '淑芬',
                   '哲瑋', '惠如', '佳樺', '思穎', '怡如', '筱涵', '雅琪', '怡安',
                   '佳玲', '心怡', '宜君', '志豪', '淑娟', '淑貞', '郁雯', '佩珊',
                   '威廷', '靜怡', '雅涵', '怡君', '靜宜', '俊賢', '雅玲', '依婷',
                   '志宏', '家豪', '詩涵', '佩君', '俊傑', '承翰', '婷婷', '淑惠',
                   '佳蓉', '俊宏', '瑋婷', '佳穎', '怡婷', '鈺婷', '雅筑', '馨儀',
                   '淑華', '柏翰', '信宏', '雅雯', '建宏', '冠宇', '佳慧', '雅慧',
                   '家瑋', '慧君', '雅惠', '婉婷', '家銘', '琬婷', '冠霖', '雅芳',
                   '郁婷', '宗翰', '淑慧', '雅婷', '宜庭', '家瑜', '惠婷',
                   '沖', '懿', '龍', '中山', '羽', '美琪', '飛', '傑克')

    last_names = ("趙", "錢", "孫", "李", "周", "吳", "鄭", "王",
                  "馮", "陳", "褚", "衛", "蔣", "沈", "韓", "楊",
                  "朱", "秦", "尤", "許", "何", "呂", "施", "張",
                  "孔", "曹", "嚴", "華", "金", "魏", "陶", "薑",
                  "戚", "謝", "鄒", "喻", "柏", "水", "竇", "章",
                  "雲", "蘇", "潘", "葛", "奚", "範", "彭", "郎",
                  "魯", "韋", "昌", "馬", "苗", "鳳", "花", "方",
                  "俞", "任", "袁", "柳", "酆", "鮑", "史", "唐",
                  "費", "廉", "岑", "薛", "雷", "賀", "倪", "湯",
                  "滕", "殷", "羅", "畢", "郝", "鄔", "安", "常",
                  "樂", "於", "時", "傅", "皮", "卞", "齊", "康",
                  "伍", "餘", "元", "蔔", "顧", "孟", "平", "黃",
                  "和", "穆", "蕭", "尹", "姚", "邵", "湛", "汪",
                  "祁", "毛", "禹", "狄", "米", "貝", "明", "臧",
                  "計", "伏", "成", "戴", "談", "宋", "茅", "龐",
                  "熊", "紀", "舒", "屈", "項", "祝", "董", "梁",
                  "杜", "阮", "藍", "閔", "席", "季", "麻", "強",
                  "賈", "路", "婁", "危", "江", "童", "顏", "郭",
                  "梅", "盛", "林", "刁", "鍾", "徐", "邱", "駱",
                  "高", "夏", "蔡", "田", "樊", "胡", "淩", "霍",
                  "虞", "萬", "支", "柯", "昝", "管", "盧", "莫",
                  "柯", "房", "裘", "繆", "幹", "解", "應", "宗",
                  "丁", "宣", "賁", "鄧", "鬱", "單", "杭", "洪",
                  "包", "諸", "左", "石", "崔", "吉", "鈕", "龔",
                  "程", "嵇", "邢", "滑", "裴", "陸", "榮", "翁",
                  "荀", "羊", "于", "惠", "甄", "曲", "封",
                  "芮", "羿", "儲", "靳", "汲", "邴", "糜", "松",
                  "井", "段", "富", "巫", "烏", "焦", "巴", "弓",
                  "牧", "隗", "山", "穀", "車", "侯", "宓", "蓬",
                  "全", "郗", "班", "仰", "秋", "仲", "伊", "宮",
                  "甯", "欒", "暴", "甘", "鈄", "曆", "戎",
                  "祖", "武", "符", "劉", "景", "詹", "束", "龍",
                  "葉", "幸", "司", "韶", "郜", "黎", "薊", "溥",
                  "印", "宿", "白", "懷", "蒲", "邰", "從", "鄂",
                  "索", "鹹", "籍", "賴", "卓", "藺", "蒙",
                  "池", "喬", "陽", "鬱", "胥", "能", "蒼", "雙",
                  "聞", "莘", "党", "翟", "譚", "貢", "勞", "逄",
                  "姬", "申", "扶", "堵", "冉", "宰", "酈", "雍",
                  "卻", "璩", "桑", "桂", "濮", "牛", "壽", "通",
                  "邊", "扈", "燕", "冀", "浦", "尚", "農",
                  "溫", "別", "莊", "晏", "柴", "瞿", "閻", "充",
                  "慕", "連", "茹", "習", "宦", "艾", "魚", "容",
                  "向", "古", "易", "慎", "戈", "廖", "庾", "終",
                  "暨", "居", "衡", "步", "都", "耿", "滿", "弘",
                  "匡", "國", "文", "寇", "廣", "祿", "闕", "東",
                  "歐", "殳", "沃", "利", "蔚", "越", "夔", "隆",
                  "師", "鞏", "厙", "聶", "晁", "勾", "敖", "融",
                  "冷", "訾", "辛", "闞", "那", "簡", "饒",
                  "曾", "毋", "沙", "養", "鞠", "須", "豐",
                  "巢", "關", "蒯", "相", "查", "後", "荊", "紅",
                  "游", "竺", "權", "逮", "盍", "益", "桓", "公",
                  "司馬", "上官", "歐陽", "東方", "公羊",
                  "公冶", "淳于", "公孫", "慕容", "司徒", "司空",)

    romanized_formats = (
        '{{first_romanized_name}} {{last_romanized_name}}',
    )

    # From https://en.wikipedia.org/wiki/Chinese_given_name#Common_Chinese_names,
    # with accents stripped
    first_romanized_names = (
        'Chao', 'Fang', 'Gang', 'Guiying', 'Jie', 'Jing', 'Juan', 'Jun', 'Lei',
        'Li', 'Min', 'Ming', 'Na', 'Ping', 'Qiang', 'Tao', 'Wei', 'Xia', 'Xiulan',
        'Xiuying', 'Yang', 'Yong', 'Yan',
    )

    # From https://en.wikipedia.org/wiki/List_of_common_Chinese_surnames
    # with accents stripped
    last_romanized_names = (
        'Bai', 'Cai', 'Cao', 'Chang', 'Chen', 'Cheng', 'Cui', 'Dai', 'Deng',
        'Ding', 'Dong', 'Du', 'Duan', 'Fan', 'Fang', 'Feng', 'Fu', 'Gao', 'Gong',
        'Gu', 'Guo', 'Han', 'Hao', 'He', 'Hou', 'Hu', 'Huang', 'Jia', 'Jiang',
        'Jin', 'Kang', 'Kong', 'Lai', 'Lei', 'Li', 'Liang', 'Liao', 'Lin', 'Liu',
        'Long', 'Lu', 'Luo', 'Ma', 'Mao', 'Meng', 'Mo', 'Pan', 'Peng', 'Qian',
        'Qiao', 'Qin', 'Qiu', 'Ren', 'Shao', 'Shen', 'Shi', 'Song', 'Su', 'Sun',
        'Tan', 'Tang', 'Tao', 'Tian', 'Wan', 'Wang', 'Wei', 'Wen', 'Wu', 'Xia',
        'Xiang', 'Xiao', 'Xie', 'Xiong', 'Xu', 'Xue', 'Yan', 'Yang', 'Yao', 'Ye',
        'Yi', 'Yin', 'Yu', 'Yuan', 'Zeng', 'Zhang', 'Zhao', 'Zheng', 'Zhong',
        'Zhou', 'Zhu', 'Zou',
    )

    def romanized_name(self):
        '''
        @example 'Chao Bai'
        '''
        pattern = self.random_element(self.romanized_formats)
        return self.generator.parse(pattern)

    def first_romanized_name(self):
        '''
        @example 'Chao'
        '''
        return self.random_element(self.first_romanized_names)

    def last_romanized_name(self):
        '''
        @example 'Chao'
        '''
        return self.random_element(self.last_romanized_names)
