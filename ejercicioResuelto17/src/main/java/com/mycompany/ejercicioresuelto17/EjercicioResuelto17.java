/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicioresuelto17;

import java.util.Scanner;

/**
 *
 * @author Mauricio
 */
public class EjercicioResuelto17 {

    public static void main(String[] args) {
        double radio,longitud_circunferencia,area_circunferencia;
        
        Scanner scanner =new Scanner(System.in);
        
        System.out.println("Ingresa el radio"); 
        radio = scanner.nextDouble();
        
        longitud_circunferencia=calculos.calcular_longitud_circulo(radio);
        area_circunferencia = calculos.calcular_area_circulo(radio);
        
        System.out.println("Lonfitud circunferencia: " + longitud_circunferencia);
        System.out.println("Area circunferencia: " + area_circunferencia);
    }
}
