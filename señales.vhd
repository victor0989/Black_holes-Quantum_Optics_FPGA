library ieee;
use ieee.std_logic_1164.all;

entity señales is
    port (
        a : in std_logic;
        b : in std_logic;
        y : out std_logic
    );
end entity señales;

architecture behavior of señales is
begin
    y <= a and b;  -- Salida es la AND de a y b
end architecture behavior;

