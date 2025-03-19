import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class Desafio_Cadastro {

	
	
	@Test
	public void DeveRealizarCadastro() {
		WebDriver driver = new FirefoxDriver();
		driver.manage().window().setSize(new Dimension(1280, 1024));
		driver.get("File:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
		driver.findElement(By.id("elementosForm:nome")).sendKeys("Lucas");
		driver.findElement(By.id("elementosForm:sobrenome")).sendKeys("Medeiros Ramos");
		driver.findElement(By.id("elementosForm:sexo:0")).click();
		driver.findElement(By.id("elementosForm:comidaFavorita:2")).click();
		WebElement element_escolaridade = driver.findElement(By.id("elementosForm:escolaridade"));
		Select combo_escolaridade = new Select(element_escolaridade);
		combo_escolaridade.selectByVisibleText("Superior");
		WebElement element_esporte = driver.findElement(By.id("elementosForm:esportes"));
		Select combo_esporte = new Select(element_esporte);
		combo_esporte.selectByVisibleText("O que eh esporte?");
		driver.findElement(By.id("elementosForm:cadastrar")).click();
		
		Assert.assertTrue(driver.findElement(By.id("resultado")).getText().startsWith("Cadastrado!"));
		Assert.assertEquals("Nome: Lucas", driver.findElement(By.id("descNome")).getText());
		Assert.assertEquals("Sobrenome: Medeiros Ramos", driver.findElement(By.id("descSobrenome")).getText());
		Assert.assertEquals("Sexo: Masculino", driver.findElement(By.id("descSexo")).getText());
		Assert.assertEquals("Comida: Pizza", driver.findElement(By.id("descComida")).getText());
		Assert.assertEquals("Escolaridade: superior", driver.findElement(By.id("descEscolaridade")).getText());
		Assert.assertEquals("Esportes: O que eh esporte?", driver.findElement(By.id("descEsportes")).getText());
		
		driver.quit();
	
}
}