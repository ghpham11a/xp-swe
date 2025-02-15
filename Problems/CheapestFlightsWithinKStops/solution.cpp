class Solution 
{
public:
    int FindCheapestPrice(int N, std::vector<std::vector<int>>& Flights, int Src, int Dst, int K) {

        std::vector<int> Prices(N, std::numeric_limits<int>::max());
        Prices[Src] = 0;

        for (int i = 0; i < K + 1; ++i)
        {
            std::vector<int> TempPrices(Prices);

            for (std::vector<int> Flight : Flights)
            {
                int FlightSrc = Flight[0];
                int FlightDst = Flight[1];
                int FlightPrice = Flight[2];

                if (Prices[FlightSrc] == std::numeric_limits<int>::max()) 
                {
                    continue;
                }

                int NewPrice = Prices[FlightSrc] + FlightPrice;
                if (NewPrice < TempPrices[FlightDst])
                {
                    TempPrices[FlightDst] = NewPrice;
                }
            }

            Prices = TempPrices;
        }

        if (Prices[Dst] == std::numeric_limits<int>::max())
        {
            return -1;
        }
        else
        {
            return Prices[Dst];
        }
    }
};