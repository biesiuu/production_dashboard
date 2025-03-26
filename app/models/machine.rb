class Machine < ApplicationRecord
  validates :name, presence: true
  validates :cycle_time, presence: true, numericality: { only_integer: true }
end
