import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.Alert;
import org.openqa.selenium.By;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Teste_Frames_E_Janelas {

	
	@Test
	public void DeveInteragirComFrame() {
		WebDriver driver = new FirefoxDriver();
		driver.manage().window().setSize(new Dimension(800, 600));
		driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");
		
		driver.switchTo().frame("frame1");
		driver.findElement(By.id("frameButton")).click();
		Alert alert = driver.switchTo().alert();
		String msg = alert.getText();
		alert.accept();
		driver.switchTo().defaultContent();
		driver.findElement(By.id("elementosForm:nome")).sendKeys(msg);
		Assert.assertEquals("Frame OK!", msg);
		
		
		
		driver.quit();
		
	}

	
	
	@Test
	public void Deve_Interagir_Com_Janela() {
		WebDriver driver = new FirefoxDriver();
		driver.manage().window().setSize(new Dimension(800, 600));
		driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");

		String janelaPrincipal = driver.getWindowHandle();
		driver.findElement(By.id("buttonPopUpEasy")).click();
		driver.switchTo().window("Popup");
		driver.findElement(By.tagName("textarea")).sendKeys("Deu Certo?");
		driver.close();
		driver.switchTo().window(janelaPrincipal);
		driver.findElement(By.tagName("textarea")).sendKeys("E agora?");
	
		driver.quit();
		
	}
	
	
	
	@Test
	public void DeveInteragir_Com_Janela_Sem_Titulo() {
		WebDriver driver = new FirefoxDriver();
		driver.manage().window().setSize(new Dimension(800, 600));
		driver.get("file:///" + System.getProperty("user.dir") + "/src/main/resources/componentes.html");

		driver.findElement(By.id("buttonPopUpHard")).click();
		System.out.println(driver.getWindowHandle());
		System.out.println(driver.getWindowHandles());
		driver.switchTo().window((String)driver.getWindowHandles().toArray()[1]);
		driver.findElement(By.tagName("textarea")).sendKeys("Deu Certo??");
		driver.switchTo().window((String)driver.getWindowHandles().toArray()[0]);
		driver.findElement(By.tagName("textarea")).sendKeys("E agora?");
	
		driver.quit();
		
	}
}