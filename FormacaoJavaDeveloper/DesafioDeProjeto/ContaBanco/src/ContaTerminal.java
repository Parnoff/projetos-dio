import java.util.Locale;
import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) throws Exception {
        
        int numero;
        String agencia, nomeCliente;
        Double saldo = 237.48;

        //criando o objeto scanner
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);

        System.out.println("Por favor, digite o número da Agência!");
        agencia = scanner.next();

        System.out.println("Agora informe o número da conta!");
        numero = scanner.nextInt();

        System.out.println("Nome completo?");
        nomeCliente = scanner.nextLine();

        System.out.println("Qual o valor do primeiro depósito?");
        saldo = scanner.nextDouble();

        System.out.println("Olá " + nomeCliente + ", obrigado por criar uma conta em nosso banco, sua agência é " + agencia + ", conta " + numero + " e seu saldo " + saldo + " já está disponível para saque.");

    }
}
