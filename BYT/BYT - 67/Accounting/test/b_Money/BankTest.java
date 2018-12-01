package b_Money;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class BankTest {
	Currency SEK, DKK;
	Bank EnglishBank, PolishBank, JapaneseBank;

	@Before
	public void setUp() throws Exception {
		DKK = new Currency("DKK", 0.20);
		SEK = new Currency("SEK", 0.15);
		EnglishBank = new Bank("EnglishBank", SEK);
		PolishBank = new Bank("PolishBank", SEK);
		JapaneseBank = new Bank("JapaneseBank", DKK);
		EnglishBank.openAccount("Jane");
		EnglishBank.openAccount("Bob");
		PolishBank.openAccount("Bob");
		JapaneseBank.openAccount("Toho");
	}

	/*
	 * Check of getName() method
	 */
	@Test
	public void GetNameTest() {
		assertEquals("EnglishBank", EnglishBank.getName());
	}

	/*
	 * Check of getCurrency() method
	 */
	@Test
	public void GetCurrencyTest() {
		assertEquals(DKK, JapaneseBank.getCurrency());
	}

	/*
	 * Check of openAccount() method
	 */
	@Test
	public void OpenAccountTest() throws AccountExistsException, AccountDoesNotExistException {
		EnglishBank.openAccount("test1");
		assertTrue(EnglishBank.existsAccount("test1"));
	}

	/*
	 * Check of deposit() method
	 */
	@Test
	public void DepositTest() throws AccountDoesNotExistException {
		EnglishBank.deposit("Bob", new Money(1000, SEK));
		assertEquals(1000, EnglishBank.getBalance("Bob"), 0);
	}

	/*
	 * Check of withdraw() method
	 */
	@Test
	public void WithdrawTest() throws AccountDoesNotExistException {
		EnglishBank.withdraw("Bob", new Money(1000, SEK));
		assertEquals(-1000, EnglishBank.getBalance("Bob"), 0);
	}

	/*
	 * Check of getBalance() method
	 */
	@Test
	public void GetBalanceTest() throws AccountDoesNotExistException {
		assertEquals(0, EnglishBank.getBalance("Bob"), 0);
	}

	/*
	 * Check of transfer() method between banks
	 */
	@Test
	public void TransferTest() throws AccountDoesNotExistException {
		EnglishBank.deposit("Bob", new Money(1000, SEK));
		EnglishBank.transfer("Bob", "Jane", new Money(500, SEK)); 
		assertEquals(500, EnglishBank.getBalance("Bob"), 0);
		assertEquals(500, EnglishBank.getBalance("Jane"), 0);

		EnglishBank.transfer("Bob", JapaneseBank, "Toho", new Money(500, SEK));
		assertEquals(0, EnglishBank.getBalance("Bob"), 0);
		assertEquals((int) (500 * 0.15 / 0.20), JapaneseBank.getBalance("Toho"), 0);
	}

	/*
	 * Check of addTimedPayment() method
	 */
	@Test
	public void TimedPaymentTest() throws AccountDoesNotExistException {
		EnglishBank.deposit("Bob", new Money(1000, SEK));
		EnglishBank.addTimedPayment("Bob", "1", 2, 0, new Money(1000, SEK), EnglishBank, "Jane"); 
		EnglishBank.tick(); 

		assertEquals(0, EnglishBank.getBalance("Bob"), 0);
		assertEquals(1000, EnglishBank.getBalance("Jane"), 0);

	}
}
