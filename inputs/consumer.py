"""
@file       consumer.py
@brief      A consumer node that receives packets and prints them.
"""

from node import Node
from plotter import Plotter

class Consumer(Node):
    """
    @class      Consumer
    """
    def __init__(self):
        """
        @brief      A constructor for the Consumer class.
        """
        super().__init__()
        self.pkts_recvd = 0
        self.log = {}

    def advance(self, cycle):
        """
        @brief      Attempt to receive packets from input ports.
        @param      cycle - an integer representing current simulation time.
        """
        self.log[cycle] = False
        for port in self.get_input_ports().values():
            pkt = port.recv_pkt(cycle)
            if pkt:
                print(f"[+] {self.get_node_id()} received packet {pkt.get_pkt_id()} on {port.get_port_id()}")
                self.pkts_recvd += 1
                self.log[cycle] = True

    def get_stats(self):
        """
        @brief      Prints the total packets received and generates a per-cycle plot.
        """
        print(f"Consumer {self.get_node_id()} received a total of {self.pkts_recvd} packets")
        plotter = Plotter(self.log, self.get_node_id())
        plotter.plot_graph("Receive")