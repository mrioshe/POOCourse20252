/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicioresuelto12;
import java.util.Scanner;
/**
 *
 * @author Mauricio
 */
public class EjercicioResuelto12 {

    public static void main(String[] args) {
        
        double horas_trabajadas,valor_hora,retencion,salario_bruto,salario_neto;
        
        Scanner scanner =new Scanner(System.in);
        
        System.out.println("Ingresa las horas trabajadas");
        horas_trabajadas = scanner.nextDouble();
        
        System.out.println("Ingresa el valor de la hora");
        valor_hora = scanner.nextDouble();
        
        System.out.println("Ingresa el porcentaje de retención en la fuente");
        retencion = scanner.nextDouble();
        
        salario_bruto=Calculos.calcular_salario_bruto(horas_trabajadas,valor_hora);
        
        retencion=Calculos.calcular_porcentaje_retencion(retencion);
        
        double valor_retencion_fuente = Calculos.calcular_retencion_fuente(retencion, salario_bruto);
        
        salario_neto = Calculos.calcular_salario_neto(salario_bruto, valor_retencion_fuente);
        
        System.out.println("Salario bruto: " + salario_bruto);
        System.out.println("Valor retención en la fuente: " + valor_retencion_fuente);
        System.out.println("Salario neto: " + salario_neto);
       
    }
}
