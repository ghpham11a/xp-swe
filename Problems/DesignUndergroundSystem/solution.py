class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.route_data = {}

    def check_in(self, id, start_station, t):
        self.check_ins[id] = (start_station, t)

    def check_out(self, id, end_station, t) :
        start, time = self.check_ins[id]
        route = (start, end_station)
        if route not in self.route_data:
            self.route_data[route] = [0, 0]
        self.route_data[route][0] += (t - time)
        self.route_data[route][1] += 1

    def get_average_time(self, start_station, end_station):
        total, count = self.route_data[(start_station, end_station)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)