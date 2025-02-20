from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.cli import CLI

class TopologiaMenor(Topo):
    """Topologia Menor: 3 roteadores e 1 host em cada extremidade"""
    def build(self):
        # Criar os roteadores
        r1 = self.addHost('r1', cls=CPULimitedHost)
        r2 = self.addHost('r2', cls=CPULimitedHost)
        r3 = self.addHost('r3', cls=CPULimitedHost)

        # Criar os links entre os roteadores
        self.addLink(r1, r2)
        self.addLink(r1, r3)
        self.addLink(r2, r3)

        # Criar os hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Conectar os hosts aos roteadores
        self.addLink(h1, r1)
        self.addLink(h2, r3)

def run_experiment():
    """Função para iniciar a rede e configurar a CLI"""
    topo = TopologiaMenor()  # Escolher a topologia Menor

    # Iniciar a rede com a topologia selecionada
    net = Mininet(topo=topo)
    net.start()

    print("Topologia Menor Criada com Sucesso")
    print("Use a CLI para testar e configurar os protocolos manualmente")
    CLI(net)  # CLI para interação manual

    # Parar a rede após interação
    net.stop()

if __name__ == '__main__':
    run_experiment()
