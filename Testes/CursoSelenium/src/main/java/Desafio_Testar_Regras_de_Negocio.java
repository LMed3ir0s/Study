import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class Desafio_Testar_Regras_de_Negocio {

	@Test
	public void Testar_Regra_do_Negocio_Nome() {
		WebDriver driver = new FirefoxDriver();
		driver.manage().window().setSize(new Dimension(800, 600));
		driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
		
		driver.findElement(By.id("elementosForm:cadastrar")).click();
		Alert alert = driver.switchTo().alert();
		Assert.assertEquals("Nome eh obrigatorio", alert.getText());
		
		driver.quit();
		}
		
	
	
		@Test
		public void Testar_Regra_do_Negocio_Sobrenome() {
			WebDriver driver = new FirefoxDriver();
			driver.manage().window().setSize(new Dimension(800, 600));
			driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
			
			driver.findElement(By.id("elementosForm:nome")).sendKeys("Lucas");
			
			driver.findElement(By.id("elementosForm:cadastrar")).click();
			Alert alert = driver.switchTo().alert();
			Assert.assertEquals("Sobrenome eh obrigatorio", alert.getText());
			driver.quit();
		}
		
		
		
		@Test
		public void Testar_Regra_do_Negocio_Sexo() {
			WebDriver driver = new FirefoxDriver();
			driver.manage().window().setSize(new Dimension(800, 600));
			driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
			
			driver.findElement(By.id("elementosForm:nome")).sendKeys("Lucas");
			driver.findElement(By.id("elementosForm:sobrenome")).sendKeys("Medeiros Ramos");
			
			driver.findElement(By.id("elementosForm:cadastrar")).click();
			Alert alert = driver.switchTo().alert();
			Assert.assertEquals("Sexo eh obrigatorio", alert.getText());
			driver.quit();			
		}
		
		
		
		@Test
		public void Testar_Regra_do_Negocio_Comida() {
			WebDriver driver = new FirefoxDriver();
			driver.manage().window().setSize(new Dimension(800, 600));
			driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
			
			driver.findElement(By.id("elementosForm:nome")).sendKeys("Lucas");
			driver.findElement(By.id("elementosForm:sobrenome")).sendKeys("Medeiros Ramos");
			driver.findElement(By.id("elementosForm:sexo:0")).click();
			driver.findElement(By.id("elementosForm:comidaFavorita:0")).click();
			driver.findElement(By.id("elementosForm:comidaFavorita:3")).click();

			
			driver.findElement(By.id("elementosForm:cadastrar")).click();
			Alert alert = driver.switchTo().alert();
			Assert.assertEquals("Tem certeza que voce eh vegetariano?", alert.getText());
			driver.quit();			
		}
		
		
		@Test
		public void Testar_Regra_do_Negocio_Esporte() {
			WebDriver driver = new FirefoxDriver();
			driver.manage().window().setSize(new Dimension(800, 600));
			driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
			
			driver.findElement(By.id("elementosForm:nome")).sendKeys("Lucas");
			driver.findElement(By.id("elementosForm:sobrenome")).sendKeys("Medeiros Ramos");
			driver.findElement(By.id("elementosForm:sexo:0")).click();
			driver.findElement(By.id("elementosForm:comidaFavorita:0")).click();
			WebElement element_esporte = driver.findElement(By.id("elementosForm:esportes"));
			Select combo = new Select(element_esporte);
			combo.selectByContainsVisibleText("Corrida");
			combo.selectByContainsVisibleText("O que eh esporte?");

			
			driver.findElement(By.id("elementosForm:cadastrar")).click();
			Alert alert = driver.switchTo().alert();
			Assert.assertEquals("Voce faz esporte ou nao?", alert.getText());
			driver.quit();			
		}
		
		
//		driver.findElement(By.id("elementosForm:nome")).sendKeys("Lucas");
//		driver.findElement(By.id("elementosForm:sobrenome")).sendKeys("Medeiros Ramos");
//		driver.findElement(By.id("elementosForm:sexo:0")).click();
//		WebElement checkbox = driver.findElement(By.tagName("checkbox"));
//		WebElement Carne = driver.findElement(By.id("elementosForm:comidaFavorita:0")).click();
//		WebElement Vegetariano = driver.findElement(By.id("elementosForm:comidaFavorita:3")).click();
		
	
	
		
	
	
	
}
