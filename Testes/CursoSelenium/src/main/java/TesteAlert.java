import java.awt.Button;
import java.time.Duration;
import java.util.List;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class TesteAlert {

//	@Test
//	public void DeveInteragircomAlertSimples(){
//		WebDriver driver = new FirefoxDriver();
//		driver.manage().window().setSize(new Dimension(1280, 1024));
//		driver.get("File:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
//		WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(15));
//        WebElement alertButton = wait.until(ExpectedConditions.elementToBeClickable(By.id("alert")));
//		alertButton.click();
//		try {
//            Thread.sleep(2000); // Espera 1 segundo para garantir que o alerta seja exibido
//        } catch (InterruptedException e) {
//            e.printStackTrace();
//        }
//		wait.until(ExpectedConditions.alertIsPresent());
//		Alert alert = driver.switchTo().alert();
//		String alertText = alert.getText();
//		Assert.assertEquals("Alert Simples", alertText);
//		alert.accept();
//        WebElement nomeField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("elementosForm:nome")));
//        nomeField.clear();
//        nomeField.sendKeys(alertText);	
//		
//		driver.quit();
//		}
	
	@Test
	public void DeveInteragircomAlertSimples(){
		WebDriver driver = new FirefoxDriver();
		driver.manage().window().setSize(new Dimension(1280, 1024));
		driver.get("File:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
		driver.findElement(By.id("alert")).click();
		Alert alert = driver.switchTo().alert();
		String alertText = alert.getText();
		Assert.assertEquals("Alert Simples", alertText);
		alert.accept();
        driver.findElement(By.id("elementosForm:nome")).sendKeys(alertText);		
		
		driver.quit();
		}
	
	
	
	@Test
	public void DeveInteragircomAlertConfirm(){
		WebDriver driver = new FirefoxDriver();
		driver.manage().window().setSize(new Dimension(1280, 1024));
		driver.get("File:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
		driver.findElement(By.id("confirm")).click();
		Alert alert = driver.switchTo().alert();
		Assert.assertEquals("Confirm Simples", alert.getText());
		alert.accept();
		Assert.assertEquals("Confirmado", alert.getText());
		alert.accept();
		
		driver.findElement(By.id("confirm")).click();
		alert = driver.switchTo().alert();
		Assert.assertEquals("Confirm Simples", alert.getText());
		alert.dismiss();
		Assert.assertEquals("Negado", alert.getText());
		alert.dismiss();				
		
		driver.quit();
		}
	
	@Test
	public void DeveInteragirComPrompt() {
		WebDriver driver = new FirefoxDriver();
		driver.manage().window().setSize(new Dimension(1280, 1024));
		driver.get("File:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
		driver.findElement(By.id("prompt")).click();
		Alert alert = driver.switchTo().alert();
		Assert.assertEquals("Digite um numero", alert.getText());
		alert.sendKeys("teste123");
		alert.accept();
		WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(3));
		Assert.assertEquals("Era teste123?", alert.getText());
		alert.accept();
		Assert.assertEquals(":D", alert.getText());
		alert.accept();
		
		driver.quit();
		
		
		
		
		
	}
}

