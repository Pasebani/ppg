require 'securerandom'
###################
help = 1
#####Many###########
system("clear")
puts "Hi There"
print "How Many Passwords :"
many = gets.chomp.to_i
####################
print "Length Of Your Passwords:"
length = gets.chomp.to_i
######Length########
while many != 0 do
	s = rand(36**length).to_s(36)
	puts "Password #{help} is: #{s}"
	many -= 1
	help += 1
end
 