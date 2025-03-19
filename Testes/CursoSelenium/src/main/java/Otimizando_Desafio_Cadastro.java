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

public class Otimizando_Desafio_Cadastro {

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
	public void DeveRealizarCadastro() {
		dsl.send_text("elementosForm:nome", "Lucas");
		dsl.send_text("elementosForm:sobrenome", "Medeiros Ramos");
		dsl.click_Radio("elementosForm:sexo:0");
		dsl.click_Radio("elementosForm:comidaFavorita:2");
		dsl.select_combo_ByVisibleText("elementosForm:escolaridade", "Superior");
		dsl.select_combo_ByVisibleText("elementosForm:esportes", "O que eh esporte?");
		dsl.click_Button("elementosForm:cadastrar"); 
		
		
		Assert.assertTrue(dsl.get_textId("resultado").startsWith("Cadastrado!"));
		Assert.assertEquals("Nome: Lucas", dsl.get_textId("descNome"));
		Assert.assertEquals("Sobrenome: Medeiros Ramos", dsl.get_textId("descSobrenome"));
		Assert.assertEquals("Sexo: Masculino", dsl.get_textId("descSexo"));
		Assert.assertEquals("Comida: Pizza", dsl.get_textId("descComida"));
		Assert.assertEquals("Escolaridade: superior", dsl.get_textId("descEscolaridade"));
		Assert.assertEquals("Esportes: O que eh esporte?", dsl.get_textId("descEsportes"));		
		}
}

