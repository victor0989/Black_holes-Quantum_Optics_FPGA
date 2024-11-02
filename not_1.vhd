----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 26.10.2024 17:31:55
-- Design Name: 
-- Module Name: not_1 - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity not_1 is
    Port ( A : in STD_LOGIC;  -- Entrada
           Y : out STD_LOGIC); -- Salida
end not_1;

architecture Behavioral of not_1 is
begin
    Y <= not A; -- Asignación de salida Y como la negación de A
end Behavioral;

