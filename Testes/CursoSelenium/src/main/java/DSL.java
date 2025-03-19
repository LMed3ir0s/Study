import java.util.ArrayList;
import java.util.List;

import org.jspecify.annotations.Nullable;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;

public class DSL {

	private WebDriver driver;
		
	public DSL(WebDriver driver) {
		super();
		this.driver = driver;
	}

	/******* Alerta *******/
	
	public void find_ElementId(String id) {
		driver.findElement(By.id(id));
	}
	

	public void find_ElementBy(By by) {
		driver.findElement(by);
	}
	
	/******* TextField and TextArea *******/
	
	public void send_textBy(By by, String texto) {
		driver.findElement(by).sendKeys(texto);
	}
		
	public void send_textId(String id_campo, String texto){
		send_textBy(By.id(id_campo), texto);
	}	
			
	public String get_value(String id_campo){
		return driver.findElement(By.id(id_campo)).getAttribute("value");
	}
	
	/******* Radio e Check *******/
	
	public void click_Radio(String id_campo) {
		driver.findElement(By.id(id_campo)).click();
	}
	
	public boolean is_Radio_Selected(String id) {
		return (driver.findElement(By.id(id)).isSelected());
	}
	
	public void click_Check(String id_campo) {
		driver.findElement(By.id(id_campo)).click();
	}
	
	public boolean is_Check_Seletected(String id) {
		return (driver.findElement(By.id(id)).isSelected());
	}
	
	/******* Combo *******/
	
	public void select_combo_ByVisibleText(String id, String value) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
//		combo.selectByIndex(2);
//		combo.selectByValue("mestrado")
		combo.selectByVisibleText(value);
	}
	
	public void select_combo_ByIndex(String id, int value) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		combo.selectByIndex(value);		
	}
	
	public void select_combo_ByValue(String id, String value) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		combo.selectByValue(value);	
	}
	
	public void deselect_combo_ByVisibleText(String id, String value) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		combo.deselectByVisibleText(value);
	}
	
	public void deselect_combo_ByIndex(String id, int value) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		combo.deselectByIndex(value);		
	}
	
	public void deselect_combo_ByValue(String id, String value) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		combo.deselectByValue(value);	
	}
	
	public String get_Selected_Value_combo(String id) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		return combo.getFirstSelectedOption().getText();
	}
	
	public List<String> get_AllSelectedValues_Combo(String id){
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		List<WebElement> allSelectedOptions = combo.getAllSelectedOptions();
		List<String> valores = new ArrayList<String>();
		for (WebElement opcao: allSelectedOptions) {
			valores.add(opcao.getText());
		}
		return valores;
	}
	
	public int get_qtd_opt_combo(String id) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		List<WebElement> options = combo.getOptions();
		return options.size();
		}
	
	public boolean check_opt_combo(String id, String opcao) {
		WebElement element = driver.findElement(By.id(id));
		Select combo = new Select(element);
		List<WebElement> options = combo.getOptions();
		for (WebElement option: options) {
			if(option.getText().equals(opcao)) {
				return true;
			}
		}
		return false;
	}
	
	/******* Button *******/
	
	public void click_Button(String id) {
		driver.findElement(By.id(id)).click();
	}

	public String get_Value_Element(String id) {
		return driver.findElement(By.id(id)).getAttribute("value");
	}
	
	/******* Link *******/
	
	public void click_link(String link) {
		driver.findElement(By.linkText(link)).click();
	}
	
	/******* Texto *******/
	
	public String get_textBy(By by) {
		return driver.findElement(by).getText();
	}
	
	public String get_textId(String id) {
		return get_textBy(By.id(id));
	}

	/******* Alerta *******/
	
	public String get_text_alert() {
		Alert alert = driver.switchTo().alert();
		return alert.getText();
	}
	
	public String get_textAccept_alert() {
		Alert alert = driver.switchTo().alert();
		String valor = alert.getText();
		alert.accept();
		return valor;		
	}
	
	public String get_textDismiss_alert() {
		Alert alert = driver.switchTo().alert();
		String valor = alert.getText();
		alert.dismiss();
		return valor;		
	}
	
	public String send_text_alertAccept(String value) {
		Alert alert = driver.switchTo().alert();
		alert.sendKeys(value);
		alert.accept();		
	}
	
	/******* Frames e Janelas *******/
	
	public void frame_enter(String id) {
		driver.switchTo().frame(id);
	}
	
	public void frame_exit() {
		driver.switchTo().defaultContent();
	}
	
	public void switch_window(String id) {
		driver.switchTo().window(id);
	}
	
	
	
	
	
	
	
	
	
	
}

