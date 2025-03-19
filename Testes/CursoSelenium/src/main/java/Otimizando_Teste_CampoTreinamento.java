import java.util.List;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class Otimizando_Teste_CampoTreinamento {
	
	private WebDriver driver;
	private DSL dsl;
	
	@Before
	public void inicializar() {
		driver = new FirefoxDriver();
		driver.manage().window().setSize(new Dimension(800, 600));
		driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
		dsl = new DSL(driver);
			
	}

	
	@After
	public void finalizar() {
		driver.quit();
	}
	
	
	
	@Test
	public void testTextField() {
		dsl.send_text("elementosForm:nome", "Teste de Escrita");
		Assert.assertEquals("Teste de Escrita", dsl.get_value("elementosForm:nome"));	
	}
	
	
	
	@Test
	public void deveInteragirComTextArea() {
		dsl.send_text("elementosForm:sugestoes", "teste_2");
		Assert.assertEquals("teste_2", dsl.get_value("elementosForm:sugestoes"));
	}
	
	
	
	@Test
	public void deveInteragirComRadioButton() {		
		dsl.click_Radio("elementosForm:sexo:0");
		Assert.assertTrue(driver.findElement(By.id("elementosForm:sexo:0")).isSelected());
	}
	
	
	
	@Test
	public void deveInteragirComCheckBox() {		
		driver.findElement(By.id("elementosForm:comidaFavorita:0")).click();
		Assert.assertTrue(dsl.check_selected("elementosForm:comidaFavorita:0"));
	}
	
	
	
	@Test
	public void deveInteragirComCombo() {		
		dsl.select_combo_ByVisibleText("elementosForm:escolaridade", "2o grau completo");
		Assert.assertEquals("2o grau completo", dsl.getValue_combo("elementosForm:escolaridade"));
	}
	
	
	
	@Test
	public void DeveVerificarValoresCombo() {
		
		WebElement element = driver.findElement(By.id("elementosForm:escolaridade"));
		Select combo = new Select(element);
		List<WebElement> options = combo.getOptions();
		Assert.assertEquals(8, options.size());
		
		boolean encontrou = false;
		for(WebElement option: options) {
			if(option.getText().equals("Doutorado")) {
				encontrou = true;
				break;
			}
		}
		
		Assert.assertTrue(encontrou);
	}
	
	
	
	@Test
	public void DeveVerificarValoresComboMultiplo() {
	
		WebElement element = driver.findElement(By.id("elementosForm:esportes"));
		Select combo = new Select(element);
//		combo.selectByVisibleText("Natacao");
//		combo.selectByVisibleText("Futebol");
//		combo.selectByVisibleText("Corrida");
		List<WebElement> options = combo.getOptions();
		for (WebElement option: options) {
			combo.selectByVisibleText(option.getText());
		}
						
		List<WebElement> allSelectedOptions = combo.getAllSelectedOptions();
		Assert.assertEquals(options.size(), allSelectedOptions.size());
	}
	
	
	
	@Test
	public void DeveInteragirComBotao() {
		dsl.click_Button("buttonSimple");
		WebElement botao = driver.findElement(By.id("buttonSimple"));
		Assert.assertEquals("Obrigado!", botao.getAttribute("value"));
	}
	
	
	
	@Test
	public void DeveInteragirComLink() {		
		dsl.click_link("Voltar");
		Assert.assertEquals("Voltou!", dsl.get_textId("resultado"));	
	}
	
	
	
	@Test
	public void DeveBuscarTextoNaPagina() {
		
//		driver.findElement(By.tagName("body"));
//		Assert.assertTrue(driver.findElement(By.tagName("body")).getText().contains("Campo de Treinamento"));
		Assert.assertEquals("Campo de Treinamento", dsl.get_textBy(By.tagName("h3")));
		Assert.assertEquals("Cuidado onde clica, muitas armadilhas...", dsl.get_textBy(By.className("facilAchar")));
	}
	
	
}
