package exam3_2_5;
import java.util.Date;

public class Account {
	private String ownerName;	//所有者
	private String accountNo;	//账号
	private double balance;		//余额
	private Date datetime;		//创建时间
	
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
	
	//存款
	public void desposit(double account){
		balance += account;
		String recordStr = String.format("%1 $ s %2 $tF %2 $ tT存款:%3 ", arg1, arg2)
	}
	
	
	
}
