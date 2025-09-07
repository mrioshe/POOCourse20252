/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicioresuelto5;
import java.util.Scanner;
/**
 *
 * @author Mauricio
 */
public class EjercicioResuelto5 {

    public static void main(String[] args) {
        double suma,x,y;
        
        Scanner scanner =new Scanner(System.in);
        
        System.out.println("Ingresa un número para la suma");
        suma = scanner.nextDouble();
        
        System.out.println("Ingresa un número para x");
        x = scanner.nextDouble();
        
        System.out.println("Ingresa un número para y");
        y = scanner.nextDouble();
        
        suma=Calculos.calcular_suma(suma,x);
        x=Calculos.calcular_x(x,y);
        
        suma=suma+(x/y);
        
        System.out.println("El valor de la suma es: " + suma);
        
    }
}
