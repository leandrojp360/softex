let Banco = new Object();
Banco.conta = "0001";
Banco.saldo = 1,500.00;
Banco.tipo = "poupança";
Banco.agencia = "123";
function saldo() {
document.write (" o saldo da " + conta + " é: " + saldo);
}
function deposito(deposito) {
saldo += deposito;
document.write(" um deposito de " + deposito + " saldo atualizado: " + saldo);
}
function saque(saque) {
saldo -= saque;
document.write(" um saque de " + saque + " saldo atualizado: " + saldo);
}
function numeroconta() {
document.write (" numedo da " + tipo + " é: " + conta);
}
let deposito = 1000.00;
deposito(deposito);
let saque = 500.00;
saque(saque);
numeroconta()
