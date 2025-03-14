import org.openqa.selenium.Point;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;

import java.awt.Dimension;

import org.junit.Assert;
import org.junit.jupiter.api.Test; 

public class TesteGoogle {
	
	@Test
	public void teste(){
		System.setProperty("webdriver.gecko.driver", "C:/Users/lucas/OneDrive/Área de Trabalho/CURSO_SELENIUM/Drivers/geckodriver.exe");
		WebDriver driver = new FirefoxDriver();
//		WebDriver driver = new ChromeDriver();
//		WebDriver driver = new InternetExplorerDriver();		
		driver.manage().window().setSize(new org.openqa.selenium.Dimension(800, 600));
		driver.manage().window().setPosition(new Point(100, 100));
		driver.get("http://www.google.com");
		System.out.println(driver.getTitle());
		Assert.assertEquals("Google",driver.getTitle());
		driver.quit();
	}
}
