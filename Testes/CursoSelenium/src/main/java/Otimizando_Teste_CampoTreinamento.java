import java.util.Arrays;
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
		dsl.send_textId("elementosForm:nome", "Teste de Escrita");
		Assert.assertEquals("Teste de Escrita", dsl.get_value("elementosForm:nome"));	
	}
	
	
	
	@Test
	public void deveInteragirComTextArea() {
		dsl.send_textId("elementosForm:sugestoes", "teste_2");
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
		Assert.assertTrue(dsl.is_Check_Seletected("elementosForm:comidaFavorita:0"));
	}
	
	
	
	@Test
	public void deveInteragirComCombo() {		
		dsl.select_combo_ByVisibleText("elementosForm:escolaridade", "2o grau completo");
		Assert.assertEquals("2o grau completo", dsl.get_Selected_Value_combo("elementosForm:escolaridade"));
	}
	
	
	
	@Test
	public void DeveVerificarValoresCombo() {
		Assert.assertEquals(8, dsl.get_qtd_opt_combo("elementosForm:escolaridade"));
		Assert.assertTrue(dsl.check_opt_combo("elementosForm:escolaridade", "Doutorado"));
	}
	
	
	
	@Test
	public void DeveVerificarValoresComboMultiplo() {
		dsl.select_combo_ByVisibleText("elementosForm:esportes", "Natacao");
		dsl.select_combo_ByVisibleText("elementosForm:esportes", "Corrida");
		dsl.select_combo_ByVisibleText("elementosForm:esportes", "O que eh esporte?");	
		 
		List<String> opt_selecionadas = dsl.get_AllSelectedValues_Combo("elementosForm:esportes");
		Assert.assertEquals(3, opt_selecionadas.size());
		
		dsl.deselect_combo_ByVisibleText("elementosForm:esportes", "Corrida");
		opt_selecionadas = dsl.get_AllSelectedValues_Combo("elementosForm:esportes");
		Assert.assertEquals(2, opt_selecionadas.size());
		Assert.assertTrue(opt_selecionadas.containsAll(Arrays.asList("Natacao", "O que eh esporte?")));
	}
	
	
	
	@Test
	public void DeveInteragirComBotao() {
		dsl.click_Button("buttonSimple");
		Assert.assertEquals("Obrigado!", dsl.get_Value_Element("buttonSimple"));
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
