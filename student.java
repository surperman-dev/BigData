package exam3_2_5;
import java.util.Date;

public class Account {
	private String ownerName;	//������
	private String accountNo;	//�˺�
	private double balance;		//���
	private Date datetime;		//����ʱ��
	
	public Account(String accountNo,String ownerName){
		this(ownerName, accountNo,0);
	}
	
	public Account(String ownerName, String accountNo, double balance) {
		super();
		this.ownerName = ownerName;
		this.accountNo = accountNo;
		this.balance = balance;
		this.datetime = new Date();
	}
	
	//���
	public void desposit(double account){
		balance += account;
		String recordStr = String.format("%1 $ s %2 $tF %2 $ tT���:%3 ", arg1, arg2)
	}
	
	
	
}
