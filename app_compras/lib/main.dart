import 'package:flutter/material.dart';

void main() {
  runApp(const MeuMercadoApp());
}

class MeuMercadoApp extends StatelessWidget {
  const MeuMercadoApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'App de Compras',
      theme: ThemeData(
        primaryColor: const Color(0xFF2196F3), // Azul sugerido para os botões
        scaffoldBackgroundColor: const Color(
          0xFFF8F9FA,
        ), // Fundo claro para descanso visual
      ),
      home: const TelaNavegacao(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class TelaNavegacao extends StatefulWidget {
  const TelaNavegacao({super.key});

  @override
  State<TelaNavegacao> createState() => _TelaNavegacaoState();
}

class _TelaNavegacaoState extends State<TelaNavegacao> {
  int _indiceAtual = 0;

  // Telas temporárias (vamos construir cada uma depois)
  final List<Widget> _telas = [
    const Center(
      child: Text('Tela 1: Minha Lista', style: TextStyle(fontSize: 24)),
    ),
    const Center(
      child: Text('Tela 2: Adicionar Produto', style: TextStyle(fontSize: 24)),
    ),
    const Center(
      child: Text('Tela 3: Meu Carrinho', style: TextStyle(fontSize: 24)),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _telas[_indiceAtual],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _indiceAtual,
        onTap: (indice) {
          setState(() {
            _indiceAtual = indice;
          });
        },
        selectedItemColor: const Color(0xFF2196F3),
        unselectedItemColor: Colors.grey,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.list), label: 'Lista'),
          BottomNavigationBarItem(
            icon: Icon(Icons.add_circle),
            label: 'Adicionar',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.shopping_cart),
            label: 'Carrinho',
          ),
        ],
      ),
    );
  }
}
