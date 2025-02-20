from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.cli import CLI

class TopologiaMaiorMalhaParcial(Topo):
    """Topologia Maior: 8 roteadores em malha parcial e 2 hosts"""
    def build(self):
        # Criar os roteadores
        r1 = self.addHost('r1', cls=CPULimitedHost)
        r2 = self.addHost('r2', cls=CPULimitedHost)
        r3 = self.addHost('r3', cls=CPULimitedHost)
        r4 = self.addHost('r4', cls=CPULimitedHost)
        r5 = self.addHost('r5', cls=CPULimitedHost)
        r6 = self.addHost('r6', cls=CPULimitedHost)
        r7 = self.addHost('r7', cls=CPULimitedHost)
        r8 = self.addHost('r8', cls=CPULimitedHost)

        # Criar os links entre os roteadores
        self.addLink(r1, r2)
        self.addLink(r1, r3)
        self.addLink(r2, r4)
        self.addLink(r2, r5)
        self.addLink(r3, r6)
        self.addLink(r3, r7)
        self.addLink(r4, r8)
        self.addLink(r5, r8)
        self.addLink(r6, r8)
        self.addLink(r7, r8)

        # Criar os hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Conectar os hosts aos roteadores
        self.addLink(h1, r1)
        self.addLink(h2, r8)

def run_experiment():
    """Função para iniciar a rede e configurar a CLI"""
    topo = TopologiaMaiorMalhaParcial()  # Escolher a topologia Maior

    # Iniciar a rede com a topologia selecionada
    net = Mininet(topo=topo)
    net.start()

    print("Topologia Maior (Malha Parcial) Criada com Sucesso")
    print("Use a CLI para testar e configurar os protocolos manualmente")
    CLI(net)  # CLI para interação manual

    # Parar a rede após interação
    net.stop()

if __name__ == '__main__':
    run_experiment()
