package Data;

import Domain.Buket;
import Domain.Order;
import Services.ShopAPI;

import java.util.List;

public class Database implements ShopAPI {
    @Override
    public List<Buket> getBuketter() {
        return null;
    }

    @Override
    public List<Order> getAllOrders() {
        return null;
    }

    @Override
    public Order getOrderById(int id) {
        return null;
    }

    @Override
    public void saveOrder(Order order) {

    }

    @Override
    public void markOrderAsDone(Order order) {

    }
}
