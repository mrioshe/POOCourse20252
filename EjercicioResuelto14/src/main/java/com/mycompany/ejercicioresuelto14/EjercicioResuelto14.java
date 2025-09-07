/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicioresuelto14;
import java.util.Scanner;
/**
 *
 * @author Mauricio
 */
public class EjercicioResuelto14 {

    public static void main(String[] args) {
        
        double numero, numero_cuadrado,numero_cubico;
        
        Scanner scanner =new Scanner(System.in);
        
        System.out.println("Ingresa el numero"); 
        numero = scanner.nextDouble();
        
        numero_cuadrado=Calculos.calcular_cuadrado(numero);
        numero_cubico = Calculos.calcular_cubo(numero);
        
        System.out.println("Número al cuadrado: " + numero_cuadrado);
        System.out.println("Número al cubo: " + numero_cubico);
        
    }
}
