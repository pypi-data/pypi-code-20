from .position_book import Position, PositionBook
from .types import *
from .order import Order
import abc
from .tick import Tick
from .bar import Bar
from .exe_rpt import ExecutionRpt


class AccountListener:
    @abc.abstractclassmethod
    def handle_order_status_cahnge(self, order, src_status):
        pass

    @abc.abstractclassmethod
    def handle_exerpt(self, rpt):
        pass


class TradeError(Exception):
    pass


class Account:
    def __str__(self):
        _str = "余额: %.2f, 冻结: %.2f 持仓: " % (
            self._balance, self._frozen_balance)
        if len(self.positions) == 0:
            _str += 'none'
        else:
            arr = map(lambda p: '%s(volume:%d,cost:%.2f,market:%.2f)' %
                      (p.symbol, p.volume, p.cost, p.market_value), self.positions)
            _str += ', '.join(arr)
        _str += ' 全部股票市值：%.2f' % self.market_value
        _str += ' 股票+现金：%.2f' % self.total_value
        return _str

    def __eq__(self, other):
        # 余额等全部相等
        if other is None or self.balance != other.balance or self.frozen_balance != other.frozen_balance:
            return False
        else:
            pos1 = self._positionBookDic
            pos2 = other._positionBookDic
            if len(pos1) != len(pos2):
                return False
            for symbol in pos1:
                if symbol not in pos2:
                    return False
                elif pos1[symbol].volume != pos2[symbol].volume:
                    return False
            return True
        return True

    def __init__(self, balance, frozen_balance=0, positions=None, bid_fee_radio=0, ask_fee_radio=0):
        self._balance = float(balance)
        self._positionBookDic = {}
        self._frozen_balance = float(frozen_balance)
        if positions is not None:
            for p in positions:
                if p.symbol not in self._positionBookDic:
                    book = PositionBook(p.symbol)
                    self._positionBookDic[p.symbol] = book
                self._positionBookDic[p.symbol].add_position(
                    p.volume, p.price, update_market_price=True)
        self._orders = []
        self._bid_fee_radio = bid_fee_radio
        self._ask_fee_radio = ask_fee_radio
        self._order_listenres = []

    @property
    def frozen_balance(self):
        '''
        冻结金额，买入下单后会冻结相关金额
        '''
        return self._frozen_balance

    @property
    def balance(self):
        '''
        可用余额
        '''
        return self._balance

    @property
    def positions(self):
        '''
        持仓列表
        '''
        return self._positionBookDic.values()

    def get_positions(self):
        '''
        返回持仓列表
        '''
        return self.positions

    def get_position(self, symbol):
        '''
        返回制定代码的持仓，如果为空，返回 None
        '''
        return self._positionBookDic[symbol] if symbol in self._positionBookDic else None

    @property
    def market_value(self):
        '''
        股票总市值，不包含现金
        '''
        return sum(map(lambda p: p.market_value, self.positions))

    @property
    def cash(self):
        '''
        现金，包含余额+冻结部分
        '''
        return self._balance + self._frozen_balance

    @property
    def total_value(self):
        '''
        总市值，包含现金
        '''
        return self.market_value + self._balance + self._frozen_balance

    @property
    def total_cost(self):
        '''
        股票总成本
        '''
        return sum(map(lambda p: p.cost, self.positions))

    def make_snapshot(self):
        '''
        创建资产快照，最好不要频繁调用
        '''
        return State({
            "balance": self._balance,
            "frozen_balance": self._frozen_balance,
            "cash": self.cash,
            "total_cost": self.total_cost,
            "market_value": self.market_value,
            "total_value": self.total_value
        })

    def get_volume_of_symbol(self, symbol):
        '''
        返回指定股票持有份额，包含所有状态
        '''
        if symbol not in self._positionBookDic:
            return 0
        return self._positionBookDic[symbol].volume

    def get_frozen_volume_of_symbol(self, symbol):
        '''
        返回指定股票被冻结的份额，卖出中
        '''
        if symbol not in self._positionBookDic:
            return 0
        return self._positionBookDic[symbol].frozen_volume

    def get_free_volume_of_symbol(self, symbol):
        '''
        返回指定股票可交易部分的份额
        '''
        if symbol not in self._positionBookDic:
            return 0
        return self._positionBookDic[symbol].free_volume

    def get_locked_volume_of_symbol(self, symbol):
        '''
        返回指定股票锁定的份额
        '''
        if symbol not in self._positionBookDic:
            return 0
        return self._positionBookDic[symbol].locked_volume

    def get_orders(self)->list:
        '''
        获取订单
        '''
        return self._orders

    @abc.abstractclassmethod
    def mk_order(self, order: Order):
        pass

    @abc.abstractclassmethod
    def cancel_order(self, order_cid):
        pass

    def add_order_listener(self, callback):
        self._order_listenres.append(callback)

    def _order_change_callback(self, order, src_status):
        for listener in self._order_listenres:
            listener.handle_order_status_cahnge(order, src_status)

    def _order_rpt(self, rpt):
        for listener in self._order_listenres:
            listener.handle_exerpt(rpt)

    def handle_events(self, _type, msg):
        pass
