import zof

APP = zof.Application('hub')


@APP.message('channel_up')
def channel_up(event):
    APP.logger.info('Channel UP datapath_id=%s', event.datapath_id)
    FLOW_MOD_TABLE_MISS.send(datapath_id=event.datapath_id)


@APP.message('packet_in')
def packet_in(event):
    APP.logger.info('Packet_in %r', event)
    PACKET_OUT.send(
        datapath_id=event.datapath_id,
        in_port=event.msg.in_port,
        data=event.msg.data)


FLOW_MOD_TABLE_MISS = zof.compile('''
  type: FLOW_MOD
  msg:
    table_id: 0
    command: ADD
    priority: 0
    match:
    instructions:
      - instruction: APPLY_ACTIONS
        actions:
          - action: OUTPUT
            port_no: CONTROLLER
            max_len: NO_BUFFER
''')

PACKET_OUT = zof.compile('''
  type: PACKET_OUT
  msg:
    in_port: $in_port
    actions:
      - action: OUTPUT
        port_no: ALL
    data: $data
''')

if __name__ == '__main__':
    zof.run()
