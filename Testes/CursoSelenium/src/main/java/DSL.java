import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;

public class DSL {

	private WebDriver driver;
	
	
//	@Before
//	public void inicializar() {
//		driver = new FirefoxDriver();
//		driver.manage().window().setSize(new Dimension(800, 600));
//		driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
//	}
//	
//	
//	@After
//	public void finalizar() {
//		driver.quit();
//	}
	
	
	
	public DSL(WebDriver driver) {
		super();
		this.driver = driver;
	}


	
	public void send_text(String id_campo, String texto){
		driver.findElement(By.id(id_campo)).sendKeys(texto);
		}
	
	
	
	public String get_value(String id_campo){
		return driver.findElement(By.id(id_campo)).getAttribute("value");
	}
	
	
	
	public void click_Radio(String id_campo) {
		driver.findElement(By.id(id_campo)).click();
	}
	
	
	
	
	public boolean check_selected(String id) {
		return (driver.findElement(By.id(id)).isSelected());
	}
	
	
	
	public void select_combo_ByVisibleText(String id, String value) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
//		combo.selectByIndex(2);
//		combo.selectByValue("mestrado")
		combo.selectByVisibleText(value);
	}
	
	
	
	public String getValue_combo(String id) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		return combo.getFirstSelectedOption().getText();
	}
	
	
	
	public void click_Button(String id) {
		driver.findElement(By.id(id)).click();
	}
	
	
	
	public void click_link(String link) {
		driver.findElement(By.linkText(link)).click();
	}
	
	public String get_textId(String id) {
		return driver.findElement(By.id(id)).getText();
	}

	

	public String get_textBy(By by) {
		return driver.findElement(by).getText();
	}
}

